import time
import multiprocessing
import telebot
from telebot import types
token="6411125766:AAGmdC3N58bcAgrLzcCLEzo-TaBoImXqVUs"
bot=telebot.TeleBot(token)
datas=["Температура снаружи","Температура внутри","Влажность снаружи","Влажность внутри","Влажность почвы","Уровень воды","Уровень освещения"]
tp=["❌","✅"]
tpDatas={}
for i in range(len(datas)):
    tpDatas[datas[i]]=0
@bot.message_handler(commands=["getGrath"])
def m(message):
    global datas
    global tpDatas
    markup=types.ReplyKeyboardMarkup()
    markup.row(types.KeyboardButton("Температура внутри"),types.KeyboardButton("Влажность внутри"))
    markup.row(types.KeyboardButton("Температура снаружи"), types.KeyboardButton("Влажность снаружи"))
    markup.row(types.KeyboardButton("Влажность почвы"), types.KeyboardButton("Уровень освещения"))
    markup.row(types.KeyboardButton("Уровень воды"))
    markup.row(types.KeyboardButton("Всё готово"))
    res=""
    for i in tpDatas:
        res+=f"{i} {tp[tpDatas[i]]}\n"
    mees=f"Пожалуйста, выберите данные, которые должны быть на графике\n{res}"
    bot.send_message(message.chat.id,mees,reply_markup=markup)
@bot.message_handler(content_types=["text"])
def txtF(message):
    global datas
    global tpDatas
    if message.text=="Температура внутри":
        tpDatas[message.text]=int(not bool(tpDatas[message.text]))
        print(tpDatas)
        res = ""
        for i in tpDatas:
            res += f"{i} {tp[tpDatas[i]]}\n"
        mees = f"Пожалуйста, выберите данные, которые должны быть на графике\n{res}"
        bot.send_message(message.chat.id,res)

    elif message.text=="Температура снаружи":
        tpDatas[message.text]=int(not bool(tpDatas[message.text]))
        print(tpDatas)
        res = ""
        for i in tpDatas:
            res += f"{i} {tp[tpDatas[i]]}\n"
        mees = f"Пожалуйста, выберите данные, которые должны быть на графике\n{res}"
        bot.send_message(message.chat.id, res)
    elif message.text=="Влажность внутри":
        tpDatas[message.text]=int(not bool(tpDatas[message.text]))
        print(tpDatas)
        res = ""
        for i in tpDatas:
            res += f"{i} {tp[tpDatas[i]]}\n"
        mees = f"Пожалуйста, выберите данные, которые должны быть на графике\n{res}"
        bot.send_message(message.chat.id,res)
    elif message.text=="Влажность снаружи":
        tpDatas[message.text]=int(not bool(tpDatas[message.text]))
        print(tpDatas)
        res = ""
        for i in tpDatas:
            res += f"{i} {tp[tpDatas[i]]}\n"
        mees = f"Пожалуйста, выберите данные, которые должны быть на графике\n{res}"
        bot.send_message(message.chat.id,res)
    elif message.text=="Уровень освещения":
        tpDatas[message.text]=int(not bool(tpDatas[message.text]))
        print(tpDatas)
        res = ""
        for i in tpDatas:
            res += f"{i} {tp[tpDatas[i]]}\n"
        mees = f"Пожалуйста, выберите данные, которые должны быть на графике\n{res}"
        bot.send_message(message.chat.id,res)
    elif message.text=="Влажность почвы":
        tpDatas[message.text]=int(not bool(tpDatas[message.text]))
        print(tpDatas)
        res = ""
        for i in tpDatas:
            res += f"{i} {tp[tpDatas[i]]}\n"
        mees = f"Пожалуйста, выберите данные, которые должны быть на графике\n{res}"
        bot.send_message(message.chat.id,res)
    elif message.text=="Уровень воды":
        tpDatas[message.text]=int(not bool(tpDatas[message.text]))
        print(tpDatas)
        res = ""
        for i in tpDatas:
            res += f"{i} {tp[tpDatas[i]]}\n"
        mees = f"Пожалуйста, выберите данные, которые должны быть на графике\n{res}"
        bot.send_message(message.chat.id,res)
    elif message.text=="Всё готово":
        audio = open(r'utrom-dengi.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()

bot.polling(none_stop=True)