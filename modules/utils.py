from telegram import Message, Bot
from telegram.ext import ContextTypes
from typing import Union

async def reply(msg: Message, text: str, **kwargs):
    """Отвечает на сообщение"""
    await msg.reply_text(text, **kwargs)

async def send_message(chat_id: int, text: str, bot: Bot, **kwargs):
    """Отправляет сообщение в указанный чат"""
    await bot.send_message(chat_id=chat_id, text=text, **kwargs)

async def send_photo(chat_id: int, photo: Union[str, bytes], bot: Bot, **kwargs):
    """Отправка фото в чат"""
    await bot.send_photo(chat_id=chat_id, photo=photo, **kwargs)

async def send_document(chat_id: int, document: Union[str, bytes], bot: Bot, **kwargs):
    """Отправка документа в чат"""
    await bot.send_document(chat_id=chat_id, document=document, **kwargs)

async def send_video(chat_id: int, video: Union[str, bytes], bot: Bot, **kwargs):
    """Отправка видео в чат"""
    await bot.send_video(chat_id=chat_id, video=video, **kwargs)
