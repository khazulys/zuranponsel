from bot.gemini_ai import ask_gemini_as_cs
from bot.handlers.state import user_data

def register(bot, logger):
    @bot.message_handler(func=lambda msg: msg.text == "Customer service")
    def handle_customer_service(msg):
        chat_id = msg.chat.id
        logger.info(f"{msg.from_user.username} memilih menu <Customer service>")

        if chat_id not in user_data:
            user_data[chat_id] = {}

        user_data[chat_id]['awaiting_cs_question'] = True
        
        bot.send_chat_action(chat_id, "typing")
        bot.reply_to(
            msg,
            "*CS Zuran Ponsel Siap Membantu!*\n\n"
            "Silakan ajukan pertanyaan kamu.\n"
            "Ketik *selesai* jika ingin keluar dari sesi Customer Service.",
            parse_mode="Markdown"
        )

    @bot.message_handler(func=lambda msg: user_data.get(msg.chat.id, {}).get("awaiting_cs_question") is True)
    def handle_cs_question(msg):
        chat_id = msg.chat.id
        question = msg.text.strip().lower()

        if question in ["selesai", "exit", "keluar", "done"]:
            user_data[chat_id]['awaiting_cs_question'] = False
            
            bot.send_chat_action(chat_id, "typing")
            bot.reply_to(
                msg,
                "🙏 Baik kak, terima kasih telah menghubungi *CS Zuran Ponsel*. Semoga harimu menyenangkan!",
                parse_mode="Markdown"
            )
            return

        try:
            answer = ask_gemini_as_cs(msg.text)
            
            bot.send_chat_action(chat_id, "typing")
            bot.reply_to(msg, answer, parse_mode="Markdown")
        except Exception as e:
            logger.error(f"Error dari Gemini: {e}")
            bot.send_message(chat_id, "maaf, terjadi kesalahan saat memproses pertanyaan Anda.")