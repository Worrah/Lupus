from time import sleep
from telegram import Message

class SmartMessage:
    def __init__(self, message: Message):
        self._msg = message
        self.chat_id = message.chat_id
        self.bot = message.get_bot()

    async def reply(self, text: str, **kwargs):
        return await self._msg.reply_text(text, **kwargs)

    async def send_message(self, text: str, **kwargs):
        return await self.bot.send_message(chat_id=self.chat_id, text=text, **kwargs)

    async def send_photo(self, file, **kwargs):
        return await self.bot.send_photo(chat_id=self.chat_id, photo=file, **kwargs)

    async def send_document(self, file, **kwargs):
        return await self.bot.send_document(chat_id=self.chat_id, document=file, **kwargs)

    async def send_video(self, file, **kwargs):
        return await self.bot.send_video(chat_id=self.chat_id, video=file, **kwargs)

    async def send_sticker(self, sticker, **kwargs):
        return await self.bot.send_sticker(chat_id=self.chat_id, sticker=sticker, **kwargs)
    
    async def send_action(self, action: str = "typing"):
        """
        action: "typing", "upload_photo", "record_video", "upload_video", "record_audio", "upload_audio", "upload_document", "find_location", "record_video_note", "upload_video_note"

        """
        
        await self.bot.send_chat_action(chat_id=self.chat_id, action=action)
        sleep(5)