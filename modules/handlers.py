from telegram import Update
from telegram.ext import ContextTypes
from modules.logger import info,warn,error
from modules.utils import SmartMessage

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой бот.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Список команд: /start, /help")

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #Объявление всяких начальных упрощающих переменных
    lupus=SmartMessage(update)
    chat_id=update.message.chat.id
    uid=update.message.from_user.id
    if lupus.message.reply_to_message:
        lupus.reply('репля')