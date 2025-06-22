from telebot import types

DENOMINATIONS = ["5.000", "10.000", "20.000", "30.000", "40.000", "50.000"]

def create_pulsa_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    for i in range(0, len(DENOMINATIONS), 2):
        row = [types.KeyboardButton(denom) for denom in DENOMINATIONS[i:i+2]]
        markup.add(*row)

    return markup

telkomsel_btn = create_pulsa_buttons
xl_btn = create_pulsa_buttons
axis_btn = create_pulsa_buttons
indosat_btn = create_pulsa_buttons
smartfreen_btn = create_pulsa_buttons
three_btn = create_pulsa_buttons