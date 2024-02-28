import configparser  # импортируем библиотеку

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings.ini")  # читаем конфиг

print(config["Twitter"]["username"])  # обращаемся как к обычному словарю!