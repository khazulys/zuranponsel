from bot.reply_button.price_btn import (
    telkomsel_btn, indosat_btn, axis_btn, xl_btn, smartfreen_btn, three_btn
)
from bot.handlers.state import user_data

OPERATORS = {
    "Telkomsel": telkomsel_btn,
    "Indosat": indosat_btn,
    "Xl": xl_btn,
    "Axis": axis_btn,
    "Smartfreen": smartfreen_btn,
    "Three": three_btn
}

def register(bot, logger):
    @bot.message_handler(func=lambda msg: msg.text in OPERATORS)
    def handle_operator_selection(message):
        chat_id = message.chat.id
        operator_name = message.text

        user_data[chat_id] = {'operator': operator_name}
        logger.info(f"{message.from_user.username} memilih operator <{operator_name}>")

        markup = OPERATORS[operator_name]()
        prompt = "Kamu mau isi pulsa berapa?"

        bot.send_chat_action(chat_id, 'typing')
        bot.reply_to(message, prompt, parse_mode="Markdown", reply_markup=markup)