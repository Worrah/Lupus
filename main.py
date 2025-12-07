from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from modules import config, handlers
from modules.logger import info,warn,error

def main():
    # создаём приложение с токеном из config
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()

    # добавляем обработчики команд
    app.add_handler(CommandHandler("start", handlers.start))
    app.add_handler(CommandHandler("help", handlers.help_command))
    app.add_handler(MessageHandler(filters.ALL, handlers.message_handler))

    # запускаем поллинг (сам управляет event loop)
    info('БОТ ЗАПУЩЕН')
    app.run_polling()
    

if __name__ == "__main__":
    main()
