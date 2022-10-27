# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
# import confic
# import telebot

# bot = telebot.TeleBot(confic.token)
# @bot.message_handler(commands=['start', 'help', 'test'])

animals = ("Жаба Гепарт Тигр Лев Капіпапа Ящірка Рак Їжак Риба Голуб")

a = input('Введіть свою тварину:')

# for animal in animals:
#     if a[-1] = animal[0]:
#         print(animal)



# while True:
#     i = input('<<< ').strip().upper()
#     if i != '':
#         c = i[-1]
#         result = re.search(f'\\s[{c}]\\w+\\s', animals)
#         if result:
#             result = result.group(0)
#             print('>>>' + result.strip() )
#             animals = re.sub(result,'This animal was used! ', animals)
#         else:
#             print('I cant find right animal! You win!')
#             break