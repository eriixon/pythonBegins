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
                raise ClientError("Server Error")

    def put(self, metric, value, timestamp=None):
        if timestamp == None:
            timestamp = str(int(time.time()))
        message = "put {0} {1} {2}\n".format(metric, value, timestamp).encode("utf-8")
        data = self.server_connect(message)

    def get(self, value):
        message = "get {0}\n".format(value).encode("utf-8")
        response = self.server_connect(message)
        if response == "ok\n\n":
            return {}
        else:
            return self.update_data(response)

    def update_data(self,raw_data):
        data_dic = {}
        data = raw_data.decode("utf8")[3:-2].split("\n")
        data_list = [l.split() for l in data]
        try:
            if data[0] == "":
                return {}
            else:
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
        except ValueError:
            raise ClientError("Mertic is not exist")
            return {}
        except Exception:
            print("Something wrong")
        return data_dic

client = Client("127.0.0.1", 8181, timeout=5)
client.put("test", 0.5, timestamp=1)
client.put("test", 0.5, timestamp=2)
client.put("test1", 0.5, timestamp=1)
# client.put("test", 2.0, timestamp=2)
# client.put("test", 0.5, timestamp=3)
# client.put("load", 3, timestamp=4)
# client.put("load", 4, timestamp=5)
#print(client.get("*"))