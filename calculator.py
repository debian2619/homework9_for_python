from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
import random


TOKEN = '5640694856:AAFUc0CClPQ1YWcdDp6eCAA4yjhXtJPo_QY'
bot = Bot(token=TOKEN)
updater = Updater(token = TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
  context.bot.send_message(update.effective_chat.id, "Привет!Я - умный калькулятор. Я умею работать с "
                                                     "рациональными и комплексными числами.Введите команду /racional,"
                                                     "если хотите считать рациональные числа или /komplex,если будем считать комплексные")


def racional_calc(update, context):
    context.bot.send_message(update.effective_chat.id, "Отлично! Вы выбрали рациональные числа.Введите первое число: ")
    return "rac"


def racional_1(update, context):
    global rac_chislo_1
    rac_chislo_1 = int(update.message.text)
    context.bot.send_message(update.effective_chat.id, "Введите второе число: ")
    return "rac_1"

def racional_2(update, context):
    global rac_chislo_2
    rac_chislo_2 = int(update.message.text)
    context.bot.send_message(update.effective_chat.id, "Введите действие: ")
    return "rac_2"

def podschet(update, context):
    global result
    result = 0
    d = update.message.text
    if d == "+":
        result = rac_chislo_1 + rac_chislo_2
        context.bot.send_message(update.effective_chat.id,f' "Результат:  " {result} ')
    if d == "-":
        result = rac_chislo_1 - rac_chislo_2
        context.bot.send_message(update.effective_chat.id,f' "Результат:  " {result} ')
    if d == "/":
        result = rac_chislo_1 / rac_chislo_2
        context.bot.send_message(update.effective_chat.id,f' "Результат:  " {result} ')
    if d == "*":
        result = rac_chislo_1 * rac_chislo_2
        context.bot.send_message(update.effective_chat.id,f' "Результат:  " {result} ')
    return ConversationHandler.END



def komplex_calc(update, context):
  context.bot.send_message(update.effective_chat.id, "Вы выбрали комплексные числа. Напомню формулу комплексного числа: z = x + i y,"
                                                       " где x, y – действительные числа,"
                                                      "i − так называемая мнимая единица. Введи действительную часть первого числа: ")
  return "komplex"


def chislo_1_otvet_1(update, context):
  global  deistv_chast
  deistv_chast = int(update.message.text)
  context.bot.send_message(update.effective_chat.id, "Принято!Теперь введи мнимую часть числа")
  return "knopka_2"



def chislo_1_otvet_2(update, context):
   global  mnim_chast
   mnim_chast = int(update.message.text)
   context.bot.send_message(update.effective_chat.id,f'{"Отлично!Первое число готово.Я понял так: "+ str(deistv_chast) + "+" + str(mnim_chast) + "i", "Теперь введи второе число,сначала его действительную часть: "}')
   return "knopka_3"

def chislo_2_otvet_1(update, context):
   global  d_chast
   d_chast = int(update.message.text)
   context.bot.send_message(update.effective_chat.id, "Принято!Теперь введи мнимую часть числа")
   return "knopka_4"

def chislo_2_otvet_2(update, context):
   global  m_chast
   m_chast = int(update.message.text)
   context.bot.send_message(update.effective_chat.id,f'{"Отлично!Второе число готово.Я понял так: " + str(d_chast) + "+" + str(m_chast) + "i","Введите действие: "}')
   return "knopka_5"

def deistvie(update, context):
   global  d_chast
   global  deistv_chast
   global m_chast
   global mnim_chast
   deis = update.message.text
   if deis == "+":
       sum_d = int(deistv_chast + d_chast)
       sum_m = int(mnim_chast + m_chast)
       context.bot.send_message(update.effective_chat.id, f'{"У меня получилось: "  + str(sum_d) + "+" + str(sum_m) + "i"}')
   if deis == "-":
       razn_d = int(deistv_chast - d_chast)
       razn_m = int(mnim_chast - m_chast)
       context.bot.send_message(update.effective_chat.id, f'{"У меня получилось: "  + str(razn_d) + "+" + str(razn_m) + "i"}')
   return ConversationHandler.END



def cancel(update, context):
    return ConversationHandler.END



start_handler = CommandHandler('start', start)
racional_calc_handler = CommandHandler('racional', racional_calc)
racional_1_handler = MessageHandler(Filters.text, racional_1)
racional_2_handler = MessageHandler(Filters.text, racional_2)
podschet_handler = MessageHandler(Filters.text, podschet)
komplex_calc_handler = CommandHandler('komplex', komplex_calc)
first_handler = MessageHandler(Filters.text, chislo_1_otvet_1)
second_handler = MessageHandler(Filters.text, chislo_1_otvet_2)
third_handler = MessageHandler(Filters.text, chislo_2_otvet_1)
fourth_handler = MessageHandler(Filters.text, chislo_2_otvet_2)
deistvie_handler = MessageHandler(Filters.text, deistvie)
cancel_handler = CommandHandler('cancel', cancel)
conv_rac_handler = ConversationHandler(entry_points=[racional_calc_handler],
                                          states={
                                               "rac": [racional_1_handler],
                                               "rac_1": [racional_2_handler],
                                               "rac_2": [podschet_handler],

                                          },
                                          fallbacks=[cancel_handler]
                                   )

conv_komplex_handler = ConversationHandler(entry_points=[komplex_calc_handler],
                                          states={
                                               "komplex": [first_handler],
                                               "knopka_2": [second_handler],
                                               "knopka_3": [third_handler],
                                               "knopka_4": [fourth_handler],
                                               "knopka_5": [deistvie_handler],

                                          },
                                          fallbacks=[cancel_handler]
                                   )
dispatcher.add_handler(start_handler)
dispatcher.add_handler(conv_rac_handler)
dispatcher.add_handler(conv_komplex_handler)

updater.start_polling()
updater.idle()