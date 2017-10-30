import asyncio

class ServerSocketException(Exception):
    pass

class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.data_store = {}

    def connection_made(self, transport):
        peer_name = transport.get_extra_info('peername')
        print('Connection from {}'.format(peer_name))
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        #self.transport.write(resp.encode())

        self.transport.write(resp)

    async def process_data(self, raw_data):
        await asyncio.sleep(1)
        data = raw_data[:-1].split()
        print(data)
        if data[0] == "get":
            pass
        elif data[0] == "put":
            metric, key, value, timestamp = data
            if key in self.data_store:
                self.data_store[key] = self.data_store[key] + [value, timestamp]
            else:
                self.data_store[key] = [value, timestamp]
        else:
            raise ServerSocketException("incorrect input")
        print(self.data_store)
        data1 = b"palm.cpu 0.5 1150864247\npalm.cpu 0.5 1150864248\neardrum.cpu 3.0 1150864250\neardrum.cpu 4.0 1150864251\neardrum.memory 4200000.0 1503320872\n\n"
        return data1


def run_server(host, port):

    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)

    server = loop.run_until_complete(coro)
    print ("Server run")

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    run_server('127.0.0.1', 8181)
