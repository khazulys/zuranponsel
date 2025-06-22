from bot.reply_button.operator_btn import operator_btn
from bot.reply_button.ewallet_btn import ewallet_btn

def register(bot, logger):
    @bot.message_handler(func=lambda message: message.text == "Isi pulsa")
    def handle_isipulsa(message):
        logger.info(f"{message.from_user.username} memilih menu <Isi pulsa>")
        
        markup = operator_btn()
        teks = "Silahkan kamu pilih operatornya terlebih dahulu"
        
        bot.send_chat_action(message.chat.id, "typing")
        bot.reply_to(message, teks, parse_mode="Markdown", reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == "Isi ewallet")
    def handle_ewallet(message):
        logger.info(f"{message.from_user.username} memilih menu <Isi ewallet>")
        
        markup = ewallet_btn()
        teks = "Silahkan ewallet yang ingin kamu isi?"
        
        bot.send_chat_action(message.chat.id, "typing")
        bot.reply_to(message, teks, reply_markup=markup)