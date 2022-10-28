from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler


bot = Bot(token='5640694856:AAFUc0CClPQ1YWcdDp6eCAA4yjhXtJPo_QY')
updater = Updater(token='5606526865:AAGFAtNAAJeOsjIVk-6X5BmmXrGxnk6bNFs')
dispatcher = updater.dispatcher


start = 0
number_first = 1
number_second = 2
operation = 3
result = 4
numberOne = ''
numberTwo = ''
oper = ''


def numbers(number):
    try:
        return int(number)
    except:
        return complex(number.replace(' ', ''))


def result(x, y, z):
    if z == '0':
        return x + y
    elif z == '1':
        return x - y
    elif z == '2':
        return x * y
    return x / y


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Добро пожаловать в бота, который умеет '
                                                       'считать комплексные и рациональные числа! Напиши 2 числа\n'
                                                       'Введи первое число: ')

    return number_first


def numberFirst(update, context):
    global numberOne
    numberOne = numbers(update.message.text)
    context.bot.send_message(update.effective_chat.id,
                             'Отлично!\nВведи второе число: ')

    return number_second


def numberSecond(update, context):
    global numberTwo
    numberTwo = numbers(update.message.text)
    board = [[InlineKeyboardButton('+', callback_data='0'), InlineKeyboardButton('-', callback_data='1')],
             [InlineKeyboardButton('*', callback_data='2'), InlineKeyboardButton(':', callback_data='3')]]
    update.message.reply_text(
        'Выбери:', reply_markup=InlineKeyboardMarkup(board))

    return operation


def operation(update, context):
    global res

    que = update.callback_query
    var = que.data
    que.answer()
    res = result(numberOne, numberTwo, var)
    que.edit_message_text(text=f'Результат: {res}')


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!')

    return ConversationHandler.END


start_handler = CommandHandler('start', start)
cancel_handler = CommandHandler('cancel', cancel)
numone_handler = MessageHandler(Filters.text, numberFirst)
numtwo_handler = MessageHandler(Filters.text, numberSecond)
oper_handler = CallbackQueryHandler(operation)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={
                                       number_first: [numone_handler],
                                       number_second: [numtwo_handler],
                                       operation: [oper_handler],
},
    fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)
print('server start')
updater.start_polling()
updater.idle()