import telebot
import scaner
from telebot import types
import config

# class SatoshiBot:

bot = telebot.TeleBot(config.token)
msg = ''
chanel_link = '-1001632221923'


# -1001726421975 ovsyanka bot
# -1001632221923
# https://api.telegram.org/bot5526701497:AAFpjQniIHnIxKNQRvFscsQBX3rtEzeQI6g/sendMessage?chat_id=@+_38_b2-70LY4MmJi&text=test
scan = scaner.ArbiScaner()

def markup_inline():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        types.InlineKeyboardButton("Change percent of profit", callback_data='fixed_profit'),
        types.InlineKeyboardButton("Change time calculation fo volume", callback_data='time_vol')
    )
    markup.add(
        types.InlineKeyboardButton("Change volume of lim", callback_data='vol_of_lim')
    )
    markup.add(
        types.InlineKeyboardButton("Start work with default settings", callback_data='start_work'),
    )
    return markup


@bot.message_handler(commands=['go'])
def start_message(message):
    scan.start_work(bot, chanel_link, 1)



@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, "Hi, let's do some money!)", reply_markup=markup_inline())

@bot.message_handler(commands=['stop'])
def stop_scaner(message):
    scan.set_infinity(0)
    bot.send_message(message.chat.id, 'Scaner was stopped')

@bot.message_handler(commands=['get_settings'])
def get_settings(message):
    bot.send_message(message.chat.id, scan.get_settings())


def change_fixed_profit(message):
    scan.set_fixed_profit(float(message.text))


def change_time_vol(message):
    scan.set_time_vol(float(message.text))


def change_vol_of_lim(message):
    scan.set_ball_in_pull(float(message.text))

@bot.callback_query_handler(func=lambda message: True)
def callback_query(call):
    if call.data == 'fixed_profit':
        msg = bot.reply_to(call.message, "Enter new value")
        bot.register_next_step_handler(msg, change_fixed_profit)

    if call.data == 'time_vol':
        msg = bot.reply_to(call.message, "Enter new value")
        bot.register_next_step_handler(msg, change_time_vol)

    if call.data == 'vol_of_lim':
        msg = bot.reply_to(call.message, "Enter new value")
        bot.register_next_step_handler(msg, change_vol_of_lim)

    if call.data == 'start_work':
        msg = bot.reply_to(call.message, "Enter '/go' to start work")


bot.infinity_polling()

