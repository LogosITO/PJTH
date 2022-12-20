from telebot import TeleBot, types
import re
from random import random

token = '5871182165:AAH0mJ8z_dWOSPpCqcq-1Ysktw1MFMLDb0s'

notes = {}
heroes = {}
events = {}
pictures = read_csv('configs/pictures.csv')

game_map = Map()
game_map.read_map_from_csv_file('configs/true_map.csv')
game_map.read_info_from_csv_file('configs/true_dop_info.csv')

bot = TeleBot(token)

@bot.message_handler(commands=['start'])
def start_game(message):
    user = message.chat.id

    notes[user] = None
    heroes[user] = Hero('Начало', -1, 'configs/hero.txt')
    events[user] = 0

    bot.send_message(user, 'Добро пожаловать в эту очаровательную игру!')

    process_state(user, notes[user])

@bot.callback_query_handler(func=lambda call: True)
def user_answer(call):
    user = call.message.chat.id
    process_answer(user, call.data)

def process_state(user, note):
    seed(0)
    hero = heroes[user]
    keyboard = types.InlineKeyboardMarkup()

    final = False
    try:
        paths = game_map.map[hero.position]
    except:
        final = True

    if not final:
        for path in paths:
            condition, room, modifier = parse_path(path)
            if hero.check_required(condition)
                keyboard.add(types.InlineKeyboardButton(text=room, callback_data=path))


    """try:
        pic = pictures[hero.position]
        picf = True
    except:
        picf = False

    if picf is True:
        photo = open(pic, 'rb')
        bot.send_photo(user, photo)"""

    bot.send_message(user, game_map.dop_info[hero.position], reply_markup=keyboard)

    if final:
        photo = open('res/finish.jpg', 'rb')
        bot.send_photo(user, photo, caption='<33')
        bot.send_message(user, text='Огромное спасибо вам за игру! Мы правда это очень ценим!\n' \
                            + 'Может мы и не оправдали чьих-то ожиданий, но лично нам наша игра нравится)')



def process_answer(user, answer):
    hero = heroes[user]
    k = hero.check_required(answer)
    if k == 'rndF':
        bot.send_message(user, 'Ой я запутался! Думаю стоит вернуться обратно!')
        notes[user] = hero.position
    elif k == 'rateF':
        bot.send_message(user, 'Что, зачем мне туда? Я так не хочу!!! НЕ ЗАСТАВЛЯЙ МЕНЯ!')
        notes[user] = hero.position
    else:
        notes[user] = answer
        new_pos = re.sub(r'\{.*?\}|\[.*?\]|', '', answer)
        if answer in game_map.map[hero.position]:
            heroes[user].position = new_pos
        else:
            bot.send_message(user, 'Вы туда ходить не можете!(')

    process_state(user, notes[user])
