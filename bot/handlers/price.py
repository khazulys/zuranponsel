from telebot import types
from bot.handlers.state import user_data

harga_map = {
    "5.000": 7000,
    "10.000": 12000,
    "20.000": 22000,
    "30.000": 32000,
    "40.000": 42000,
    "50.000": 52000
}

def register(bot, logger):
    @bot.message_handler(func=lambda msg: msg.text in harga_map)
    def handle_nominal(msg):
        chat_id = msg.chat.id
        nominal = msg.text
        harga = harga_map[nominal]

        user_data[chat_id]['nominal'] = nominal
        user_data[chat_id]['harga'] = harga

        username = msg.from_user.username or msg.from_user.first_name
        logger.info(f"{username} memilih nominal <{nominal}>")

        # Tentukan jenis transaksi: Pulsa atau E-Wallet
        is_ewallet = 'ewallet' in user_data[chat_id]
        tipe = "e-wallet" if is_ewallet else "pulsa"

        # Kalimat sesuai konteks
        prompt = f"Masukkan nomor HP {tipe} yang ingin diisi:"

        markup = types.ForceReply(selective=False)
        bot.send_chat_action(chat_id, "typing")
        bot.reply_to(msg, prompt, reply_markup=markup)