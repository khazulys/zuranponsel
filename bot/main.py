import telebot
from dotenv import load_dotenv
import os
from bot.handlers import start, menu, operator, price, nomor_hp, handler_ewallet, customer_service
from bot.logger import setup_logger
from keep_alive import keep_alive

load_dotenv()

logger = setup_logger("main")
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

start.register(bot, logger)
operator.register(bot, logger)
menu.register(bot, logger)
price.register(bot, logger)
nomor_hp.register(bot, logger)
handler_ewallet.register(bot, logger)
customer_service.register(bot, logger)

def main():
    logger.info("bot running!")
    keep_alive()
    while True:
        try:
            bot.infinity_polling()
        except Exception:
            logger.error("Terjadi kesalahan saat polling", exc_info=True)
