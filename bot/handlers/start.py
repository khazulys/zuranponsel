from bot.reply_button.reply_btn import get_main_menu

def register(bot, logger):
    @bot.message_handler(commands=['start'])
    def start_handler(message):
        userid = message.from_user.id
        username = message.from_user.username
        logger.info(f"/start dari @{username} (id={userid})")
        markup = get_main_menu()
        
        bot.send_chat_action(message.chat.id, "typing")
        bot.reply_to(message, f"Hai @{username}, Kamu mau beli apa?", reply_markup=markup)