from client import Client


class BbdsPipeSvc(Client):
    def __init__(self):
        super(BbdsPipeSvc, self).__init__(__name__, '', '1.1')


BbdsPipeSvc().invoke({'request': 'request'})

import socket

socket.socket()