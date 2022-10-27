from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import confic
import telebot

bot = telebot.TeleBot(confic.token)

def markup_inline():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Hello", callback_data="Hello"))
    return markup



def send_welcome(message):
    markup = ReplyKeyboardMarkup(row_width=2)
    itembtn1 = KeyboardButton('🧌')
    itembtn2 = KeyboardButton('😇')
    itembtn3 = KeyboardButton('🫠')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Choose one emoji:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True) #ця функція робить дію на натискання інлайн кнопки
def callback_query(call):
    if call.data == "Hello":
        bot.send_message(call.from_user.id, "Hello-hello")

@bot.message_handler(commands=['start', 'help', 'test'])

@bot.message_handler(content_types=['text'])
def conversation(message):
    if message.text == "🧌":
        bot.send_message(message.chat.id, "U have been gnomed")
    if message.text == "😇":
        bot.send_message(message.chat.id, "Angel beauty")
    if message.text == "🫠":
        bot.send_message(message.chat.id, "Burning")
    else:
        bot.send_message(message.chat.id, "Тут інлайн кнопка", reply_markup=markup_inline())




#     mess = f'Hello, <b>{message}</b>'
#     bot.send_message(message.chat.id, mess, parse_mode='html')
#
bot.polling(non_stop=True)