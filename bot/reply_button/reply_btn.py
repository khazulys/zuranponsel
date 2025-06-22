from telebot import types

def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Isi pulsa")
    btn2 = types.KeyboardButton("Isi ewallet")
    btn3 = types.KeyboardButton("Customer service")
    markup.add(btn1, btn2)
    markup.add(btn3)
    return markup