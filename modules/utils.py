from telegram import Message, Update, User
from telegram.ext import ContextTypes
import asyncio

class SmartMessage:
    def __init__(self, update: Update):
        """
        chat_id, thread_id, user, user_mention,  bot,
        """
        self._update = update
        self.chat_id = update.effective_chat.id if update.effective_chat else None
        self.thread_id = update.effective_message.message_thread_id
        self.user: User = update.effective_user
        self.user_mention = self.user.mention_html()
        
        # Бот
        if hasattr(update, "get_bot"):
            self.bot = update.get_bot()
        elif hasattr(update, "bot"):
            self.bot = update.bot
        else:
            self.bot = None

        # Если апдейт содержит сообщение
        self.message: Message | None = update.effective_message


    async def send_action(self, action: str = "typing"):
        """
        action: "typing", "upload_photo", "record_video", "upload_video", "record_audio", "upload_audio", "upload_document", "find_location", "record_video_note", "upload_video_note"

        """
        if self.bot and self.chat_id:
            await self.bot.send_chat_action(chat_id=self.chat_id, action=action)

    async def reply(self, text: str, **kwargs):
        if self.message:
            await self.send_action("typing")
            await self.message.reply_text(text, **kwargs)

    async def send_message(self, text: str, **kwargs):
        if self.bot and self.chat_id:
            await self.send_action("typing")
            await self.bot.send_message(chat_id=self.chat_id, text=text, **kwargs)

    async def send_photo(self, file, **kwargs):
        if self.bot and self.chat_id:
            await self.send_action("upload_photo")
            await self.bot.send_photo(chat_id=self.chat_id, photo=file, **kwargs)

    async def send_document(self, file, **kwargs):
        if self.bot and self.chat_id:
            await self.send_action("upload_document")
            await self.bot.send_document(chat_id=self.chat_id, document=file, **kwargs)

    async def send_video(self, file, **kwargs):
        if self.bot and self.chat_id:
            await self.send_action("upload_video")
            await self.bot.send_video(chat_id=self.chat_id, video=file, **kwargs)

    async def send_sticker(self, sticker, **kwargs):
        if self.bot and self.chat_id:
            await self.send_action("typing")
            await self.bot.send_sticker(chat_id=self.chat_id, sticker=sticker, **kwargs)

    async def reply_typing(self, text: str, typing_time: float = 2.0, **kwargs):
        """Показывает 'печатает...' заданное время, затем отправляет текст"""
        if self.message and self.bot:
            await self.send_action("typing")
            await asyncio.sleep(typing_time)
            await self.message.reply_text(text, **kwargs)
