import asyncio
import os
import tempfile


class ServerSocketException(Exception):
    pass


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peer_name = transport.get_extra_info('peername')
        print('Connection from {}'.format(peer_name))
        self.transport = transport

    def data_received(self, data):
        response = self.process_data(data.decode())
        self.transport.write(response.encode())

    def process_data(self, raw_data):
        data = raw_data[:-1].split()
        file = os.path.join(tempfile.gettempdir(), 'db.txt')
        if data[0] == "get":
            rsp = self.read_data_db(data, file)
        elif data[0] == "put":
            rsp = self.write_data_db(data, file)
        else:
            rsp = "error\nwrong command\n\n"
        return rsp

    @staticmethod
    def write_data_db(data, file):
        print("step 1")
        with open(file, 'a') as db:
            db.write("{} {} {}\n".format(data[1], data[2], data[3]))
        print("step 2")
        return "ok\n\n"

    @staticmethod
    def read_data_db(data, file):
        rsp = 'ok\n'
        with open(file, 'r') as db:
            db_data = db.readlines()
            for item in db_data:
                if data[1] == "*":
                    rsp = "{0}{1}".format(rsp, item)
                if data[1] in item:
                    rsp = "{0}{1}".format(rsp, item)
            rsp = "{0}\n".format(rsp)
        return rsp


def run_server(host, port):
    loop = asyncio.get_event_loop()
    work = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(work)
    print("Server run")

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()

    os.remove(os.path.join(tempfile.gettempdir(), 'db.txt'))
    loop.run_until_complete(server.wait_closed())
    loop.close()



# if __name__ == '__main__':
#     run_server('127.0.0.1', 8888)
