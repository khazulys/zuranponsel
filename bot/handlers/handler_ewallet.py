from bot.reply_button.price_btn import create_pulsa_buttons
from bot.handlers.state import user_data

def register(bot, logger):
    @bot.message_handler(func=lambda message: message.text in ["Dana", "Ovo", "Shoopepay", "Linkaja", "Gopay"])
    def handle_ewallet(message):
        chat_id = message.chat.id
        ewallet = message.text
        
        user_data[chat_id] = {'ewallet': ewallet}
        logger.info(f"{message.from_user.username} memilih e-wallet <{ewallet}>")

        markup = create_pulsa_buttons()
        prompt = f"Kamu mau isi saldo {ewallet} berapa?"

        bot.send_chat_action(chat_id, 'typing')
        bot.reply_to(message, prompt, parse_mode="Markdown", reply_markup=markup)