import asyncio
from collections import deque

class ServerSocketException(Exception):
    pass

class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peer_name = transport.get_extra_info('peername')
        print('Connection from {}'.format(peer_name))
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, raw_data):
        data = raw_data[:-1].split()
        if data[0] == "get":
            rsp = self.read_data_db(data)
        elif data[0] == "put":
            rsp = self.write_data_db(data)
        else:
            raise ServerSocketException("incorrect input")
        return rsp

    @staticmethod
    def write_data_db(data):
        with open("db.txt", 'a') as db:
            db.write("{} {} {}\n".format(data[1], data[2], data[3]))
        return "ok\n"

    @staticmethod
    def read_data_db(data):
        rsp = 'ok\n'
        with open("db.txt", 'r') as db:
            for item in db.readlines():
                if data[1] in item:
                    rsp = "{0}{1}".format(rsp,item)
            rsp = "{0}\n".format(rsp)
        print("*****",rsp)
        return rsp

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)

    server = loop.run_until_complete(coro)
    print("Server run")

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    run_server('127.0.0.1', 8181)
