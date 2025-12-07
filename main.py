from telegram.ext import ApplicationBuilder, CommandHandler
from modules import config, handlers
from modules.logger import info, warn, error
async def main():
    # создаём приложение с токеном из config
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()

    # добавляем обработчики команд
    app.add_handler(CommandHandler("start", handlers.start))
    app.add_handler(CommandHandler("help", handlers.help_command))

    error('ЖОПА')
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

