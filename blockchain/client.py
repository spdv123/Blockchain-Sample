# -*- coding: utf-8 -*-
'''
矿工
'''

from miner import BitcoinMiner
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

class RClient(Protocol):
    '''
    Real client 真正的操作
    '''
    def connectionMade(self):
        print self.transport.client, '建立了连接'

    def dataReceived(self, data):
        print data

class Client(Protocol):
    '''
    负责一些初始化操作
    '''
    def __init__(self, clientID, rnd, port):
        '''
        clientID 矿工的ID, SHA256的随机数
        rnd 神秘字符串
        port 监听端口
        '''
        self.clientID = clientID
        self.rnd = rnd
        self.miner = BitcoinMiner(clientID)

        self.factory = Factory()
        self.factory.protocol = RClient
        reactor.listenTCP(port, self.factory)
        reactor.run()


if __name__ == '__main__':
    client = Client('123', '123', 22001)
    #client
