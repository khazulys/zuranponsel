from telebot import types

def ewallet_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Dana", "Ovo", "Shoopepay", "Linkaja", "Gopay"]
    
    # Tambahkan dua tombol per baris
    for i in range(0, len(buttons), 2):
        row = [types.KeyboardButton(b) for b in buttons[i:i+2]]
        markup.add(*row)

    # Kalau jumlah tombol ganjil, tombol terakhir akan ditampilkan sendirian
    return markup