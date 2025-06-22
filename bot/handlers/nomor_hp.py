from bot.midtrans_payment.payment import create_midtrans_payment_link
from telebot import types
from bot.handlers.state import user_data

def register(bot, logger):
    @bot.message_handler(func=lambda msg: msg.reply_to_message and "Masukkan nomor HP" in msg.reply_to_message.text)
    def handle_nomor_hp(msg):
        chat_id = msg.chat.id
        user_data[chat_id]['no_hp'] = msg.text

        data = user_data[chat_id]
        no_hp = data.get("no_hp")
        nominal = data.get("nominal")
        harga = data.get("harga")
        operator = data.get("operator")
        ewallet = data.get("ewallet")

        user_id = msg.from_user.id
        username = msg.from_user.username or msg.from_user.first_name

        # Buat link pembayaran
        link, order_id = create_midtrans_payment_link(
            user_id=user_id,
            username=username,
            nominal=nominal,
            no_hp=no_hp,
            total_price=harga
        )

        logger.info(f"Link pembayaran dibuat: {link}")

        # Tombol inline untuk bayar dan batal
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton("Bayar Sekarang", url=link),
            types.InlineKeyboardButton("Batal", callback_data="batal_pembelian")
        )

        # Tentukan jenis produk (Pulsa atau E-Wallet)
        produk = operator if operator else ewallet
        jenis = "Pulsa" if operator else "E-Wallet"

        # Format rincian pembelian
        rincian = (
            f"*Rincian Pembelian {jenis}*\n\n"
            f"Nomor HP     : `{no_hp}`\n"
            f"{'Operator' if operator else 'E-Wallet'} : *{produk}*\n"
            f"Nominal       : *{nominal}*\n"
            f"Harga Bayar   : *Rp {harga:,}*\n\n"
            f"Klik tombol di bawah ini untuk melanjutkan:"
        )

        bot.send_chat_action(chat_id, "typing")
        bot.reply_to(msg, rincian, parse_mode="Markdown", reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: call.data == "batal_pembelian")
    def handle_batal(call):
        chat_id = call.message.chat.id
        message_id = call.message.message_id

        try:
            bot.delete_message(chat_id, message_id)
        except Exception as e:
            logger.warning(f"Gagal menghapus pesan: {e}")

        user_data.pop(chat_id, None)
        bot.send_message(chat_id, "🙏 Terima kasih sudah berbelanja.")
        bot.answer_callback_query(call.id, text="Pembelian dibatalkan.")