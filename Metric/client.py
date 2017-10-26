import time
import socket
from operator import itemgetter


class ClientError(Exception):
    def __init__(self, text=None):
        print("Client error: ", text)


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def server_connect(self, message):
        with socket.create_connection((self.host, self.port),self.timeout) as s:
            print("Established connection with the server.")
            try:
                s.sendall(message)
                data = s.recv(1024)
                return data.decode("utf8")
            except socket.timeout:
                print("send data timeout")
            except socket.error as ex:
                raise ClientError(ex)


    def put(self, metric, value, timestamp=None):
        if timestamp == None:
            timestamp = str(int(time.time()))
        message = f"put {metric} {value} {timestamp}\n"
        data = self.server_connect(message)


    def get(self, value):
        message = "get {0}\n".format(value).encode("utf-8")
        responce = self.server_connect(message)
        if responce == "ok\n\n":
            return {}
        else:
            return self.update_data(responce)


    def update_data(self,raw_data):
        data_dic = {}
        data_list = [l.split() for l in raw_data[4:-4].split("\n")]
        print(data_list)
        try:
            for section in data_list:
                if section[0] in data_dic:
                    data_dic[section[0]] = data_dic[section[0]] + [(section[2], section[1])]
                else:
                    data_dic[section[0]] = [(section[2], section[1])]

            for key, value in data_dic.items():
                value.sort(key=itemgetter(1))

            return data_dic
        except:
            print(raw_data)

