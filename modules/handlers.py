from telegram import Update
from telegram.ext import ContextTypes
from modules.logger import info,warn,error

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой бот.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Список команд: /start, /help")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg: Message = update.effective_message
    user = update.effective_user

    # Логируем автора и текст/медиа
    msg_type = "текст" if msg.text else "медиа"
    info(f"{user.username} ({user.id}) прислал {msg_type}")

    # Реплай
    if getattr(msg, "reply_to_message", None):
        info(f"Это ответ на сообщение от {msg.reply_to_message.from_user.username}")

    # Форварды
    if getattr(msg, "forward_from", None) or getattr(msg, "forward_from_chat", None) or getattr(msg, "forward_sender_name", None):
        info("Это пересланное сообщение")

    # Обработка текстовых сообщений
    if getattr(msg, "text", None):
        await msg.reply_text(f"Вы написали: {msg.text}")

    # Обработка медиа
    elif getattr(msg, "photo", None):
        await msg.reply_text("Вы отправили фото!")
    elif getattr(msg, "video", None):
        await msg.reply_text("Вы отправили видео!")
    elif getattr(msg, "sticker", None):
        await msg.reply_text("Это стикер!")
    elif getattr(msg, "document", None):
        await msg.reply_text("Вы отправили документ!")
    else:
        await msg.reply_text("Получено сообщение неизвестного типа")