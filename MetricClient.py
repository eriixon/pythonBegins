import asyncio
import time

class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def get(self, value):
        #get <key>\n
        #return dictonary
        return value

    #Клиент получает данные в текстовом виде, метод get должен возвращать словарь с полученными ключами с сервера.
    #Значением ключа в словаре является список кортежей[(timestamp, metric_value), ...], отсортированный
    #по timestamp от меньшего к большему.
    #Значение timestamp должно быть преобразовано к целому числу int.
    #Значение метрики metric_value нужно преобразовать к числу с плавающей точкой float.

    def put(self, key, value, timestamp=None):
        if timestamp == None:
            timestamp = str(int(time.time()))
        metric = "put {0} {1} {3}\n\n".format(key, value, timestamp)
        #put <key> <value> <timestamp>\n


client = Client("127.0.0.1", 8888, timeout=15)

client.put("palm.cpu", 0.5, timestamp=1150864247)
client.put("palm.cpu", 2.0, timestamp=1150864248)
client.put("palm.cpu", 0.5, timestamp=1150864248)

client.put("eardrum.cpu", 3, timestamp=1150864250)
client.put("eardrum.cpu", 4, timestamp=1150864251)
client.put("eardrum.memory", 4200000)

print(client.get("*"))
