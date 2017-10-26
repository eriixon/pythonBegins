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
            try:
                s.sendall(message)
                data = s.recv(1024)
                return data
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
        response = self.server_connect(message)
        if response == "ok\n\n":
            return {}
        else:
            r = self.update_data(response)
            print("Client side:", r)
            return r


    def update_data(self,raw_data):
        data_dic = {}
        data = raw_data.decode("utf8")[3:-2].split("\n")
        data_list = [l.split() for l in data]
        for item in data_list:
            print(item[0], " * ", item[1], " * ",item[2])
        try:
            for item in data_list:
                key, v, t = item
                t = int(t)
                v = float(v)
                if key in data_dic:
                    data_dic[key] = data_dic[key] + [(t, v)]
                else:
                    data_dic[key] = [(t, v)]

            for key, value in data_dic.items():
                value.sort(key=itemgetter(0))
        except ClientError:
            print("Something wrong")
        print("$$$$$$$$$$$$$$$$$$$$$$   Data Dic: ", data_dic)
        return data_dic
