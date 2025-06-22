from telebot import types

def operator_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Telkomsel")
    btn2 = types.KeyboardButton("Indosat")
    btn3 = types.KeyboardButton("Xl")
    btn4 = types.KeyboardButton("Axis")
    btn5 = types.KeyboardButton("Smartfreen")
    btn6 = types.KeyboardButton("Three")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5, btn6)
    
    return markup