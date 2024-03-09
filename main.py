import time
import multiprocessing
import telebot
token="6411125766:AAGmdC3N58bcAgrLzcCLEzo-TaBoImXqVUs"
bot=telebot.TeleBot(token)
@bot.message_handler(commands=["getGrath"])
def getGrathData(message):
    bot.send_message(message.chat.id,"Пожалйста введите необходимые значения, которые нужны на графике")
    bot.register_next_step_handler(check,message)
def check(message):
    bot.send_message(message.chat.id,f"Вы выбрали {message.text}")

def task(n=100_000_000):
    while n:
        n -= 1
    print("hello")
    bot.polling(none_stop=True)

if __name__  ==  '__main__':
    start = time.perf_counter()

    p1 = multiprocessing.Process(target=task)
#    p2 = multiprocessing.Process(target=task)

    p1.start()
#    p2.start()

#    p1.join()
#    p2.join()

    finish = time.perf_counter()

    print(f'Выполнение заняло {finish-start: .2f} секунд.')