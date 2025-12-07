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

    # Тип сообщения
    msg_type = "текст" if msg.text else "медиа"
    info(f"{user.username} ({user.id}) прислал {msg_type}")

    # Проверка реплая
    if msg.reply_to_message:
        info(f"Это ответ на сообщение от {msg.reply_to_message.from_user.username}")

    # Проверка форварда
    if msg.forward_from or msg.forward_from_chat:
        info("Это пересланное сообщение")

    # Обработка текста
    if msg.text:
        await msg.reply_text(f"Вы написали: {msg.text}")

    # Обработка медиа
    elif msg.photo:
        await msg.reply_text("Вы отправили фото!")
    elif msg.video:
        await msg.reply_text("Вы отправили видео!")
    elif msg.sticker:
        await msg.reply_text("Это стикер!")
    elif msg.document:
        await msg.reply_text("Вы отправили документ!")
    else:
        await msg.reply_text("Получено сообщение неизвестного типа")