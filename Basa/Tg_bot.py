import telebot
import operations
from logging_ import logging
from menu import pb_menu, calc_menu, calc_input_tip
from pb_file_writing import create_note, delete_note
from pb_output import print_note, print_phonebook


bot = telebot.TeleBot('TOKEN')
oper = ''

def call_print_note(sep):
    @bot.message_handler()
    def call_out_note(message):
        bot.send_message(message.chat.id, print_note(message.text, sep))
        phonebook(message)

def call_print_phonebook(message, sep):
        bot.send_message(message.chat.id, print_phonebook(sep))
        phonebook(message)

@bot.message_handler(commands = ['menu'])
def menu(message):
    bot.send_message(message.chat.id,  f'Выбери нужную функцию:\n\n' \
                                       f'/calc - калькулятор вещественных и комплексных чисел\n' \
                                       f'/phonebook - телефонная книга')

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\n'\
                                      f'Я бот, который кое-что умеет.')
    menu(message)

@bot.message_handler(commands=['calc'])
def calc(message):
    bot.send_message(message.chat.id, calc_menu())

    @bot.message_handler(commands=['addition'])
    def addition(message):
        global oper
        oper = '+'
        bot.send_message(message.chat.id, calc_input_tip())

    @bot.message_handler(commands=['subtraction'])
    def subtraction(message):
        global oper
        oper = '-'
        bot.send_message(message.chat.id, calc_input_tip())

    @bot.message_handler(commands=['multiplication'])
    def multiplication(message):
        global oper
        oper = '*'
        bot.send_message(message.chat.id, calc_input_tip())

    @bot.message_handler(commands=['division'])
    def division(message):
        global oper
        oper = '/'
        bot.send_message(message.chat.id, calc_input_tip())

    @bot.message_handler(commands=['log'])
    def log(message):
        text_log = ''
        with open('log.txt', 'r') as log_f:
            for i in log_f:
                text_log += i
            bot.send_message(message.chat.id, text_log)
        calc(message)

    @bot.message_handler()
    def calculator(message):
        numbers = operations.convert_arr(message.text.split())
        result = operations.call_operation(numbers[0], numbers[1], oper)
        out = f'{numbers[0]} {oper} {numbers[1]} = {result}'
        bot.send_message(message.chat.id, out)
        logging(out)
        calc(message)


@bot.message_handler(commands = ['phonebook'])
def phonebook(message):
    bot.send_message(message.chat.id, pb_menu())

    @bot.message_handler(commands=['add_note'])
    def add_note(message):
        bot.send_message(message.chat.id, 'Введи запись в формате:\nФамилия Имя Телефон Описание')
        @bot.message_handler()
        def call_add_note(message):
            new_note = message.text.split()
            #try:
            create_note(new_note)
            bot.send_message(message.chat.id, 'Данные записаны.')
            #except:
                #bot.send_message(message.chat.id, 'Неверно введены данные.')
            phonebook(message)

    @bot.message_handler(commands=['del_note'])
    def del_note(message):
        bot.send_message(message.chat.id, 'Введи ID записи, которую нужно удалить.')
        @bot.message_handler()
        def call_delete_note(message):
            delete_note(message.text)
            bot.send_message(message.chat.id, 'Данные удалены.')
            phonebook(message)

    @bot.message_handler(commands=['row_out'])
    def row_out(message):
        bot.send_message(message.chat.id, 'Введи ID записи, которую нужно вывести.')
        call_print_note(' ')

    @bot.message_handler(commands=['col_out'])
    def col_out(message):
        bot.send_message(message.chat.id, 'Введи ID записи, которую нужно вывести.')
        call_print_note('\n')

    @bot.message_handler(commands=['row_pb'])
    def row_pb(message):
        call_print_phonebook(message, ' ')

    @bot.message_handler(commands=['col_pb'])
    def row_pb(message):
        call_print_phonebook(message, '\n')


bot.polling(none_stop=True)