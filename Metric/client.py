import time
import socket


class ClientError(Exception):
    def __init__(self, text):
        ClientError.txt = text


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def server_connect(self, message):
        with socket.create_connection((self.host, self.port),self.timeout) as s:
            try:
                s.sendall(message)
                s.timeout(1)
                data = s.recv(1024)
            except socket.timeout:
                print("send data timeout")
            except socket.error as ex:
                print("send data error:", ex)
            return data.decode("utf8")


    def put(self, key, value, timestamp=None):

        if timestamp == None:
            timestamp = str(int(time.time()))
        message = "put {0} {1} {2}\n\n".format(key, value, timestamp)
        data = self.server_coonect(message)
        if data != "ok\n\n":
            raise ClientError

    def get(self, value):
        message = "get {0}\n".format(value)
        data = self.server_coonect(message)
        if data == "ok\n\n":
            return {}
        return data

        # Клиент получает данные в текстовом виде, метод get должен возвращать словарь с полученными ключами с сервера.
        # Значением ключа в словаре является список кортежей[(timestamp, metric_value), ...], отсортированный
        # по timestamp от меньшего к большему.
        # Значение timestamp должно быть преобразовано к целому числу int.
        # Значение метрики metric_value нужно преобразовать к числу с плавающей точкой float.
