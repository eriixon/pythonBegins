import time
import asyncio


class ClientError(Exception):
    def __init__(self, text):
        ClientError.txt = text


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    async def tcp_echo_client_put(self, message, loop):
        reader, writer = await asyncio.open_connection(self.host, self.port, loop=loop)
        print("send: %r" % message)
        writer.write(message.encode())
        writer.close()
        data = await reader.read(100)
        print('Received: %r' % data.decode())
        await asyncio.sleep(1.0)
        return data

    def put(self, key, value, timestamp=None):
        if timestamp == None:
            timestamp = str(int(time.time()))
        message = "put {0} {1} {2}\n\n".format(key, value, timestamp)
        loop = asyncio.get_event_loop()
        data = loop.run_until_complete(self.tcp_echo_client_put(message, loop))
        loop.close()
        if data != "ok\n\n":
            raise ClientError

    def get(self, value):
        message = "get {0}\n".format(value)
        loop = asyncio.get_event_loop()
        data = loop.run_until_complete(self.tcp_echo_client_put(message, loop))
        loop.close()
        if data == "ok\n\n":
            return {}
        return data

    #Клиент получает данные в текстовом виде, метод get должен возвращать словарь с полученными ключами с сервера.
    #Значением ключа в словаре является список кортежей[(timestamp, metric_value), ...], отсортированный
    #по timestamp от меньшего к большему.
    #Значение timestamp должно быть преобразовано к целому числу int.
    #Значение метрики metric_value нужно преобразовать к числу с плавающей точкой float.

