import logging
import sys
from logging.handlers import RotatingFileHandler

# Настройка формата логов
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Создаём логгер
logger = logging.getLogger("lupus_bot")
logger.setLevel(logging.INFO)  # Можно DEBUG для детальной информации
warn = logger.warning
info = logger.info
error = logger.error
# Поток для консоли
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))
logger.addHandler(console_handler)

# Поток для файла с ротацией (5 файлов по 1МБ)
file_handler = RotatingFileHandler(
    "logs/bot.log", maxBytes=1_000_000, backupCount=5
)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))
logger.addHandler(file_handler)

