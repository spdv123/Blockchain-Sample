# -*- coding: utf-8 -*-

class RWer():
    def __init__(self,selfID):
        self.selfID=selfID
    def save(self,clientID,randnum,hashnum):
        try:
            f=open("./out/" + self.selfID,"a")
            f.write("=======================================\n")
            f.write("clientID:%s\n"%clientID)
            f.write("randnum:%s\n"%randnum)
            f.write("hashnum:%s\n"%hashnum)
            f.write("=======================================\n")
            print("成功记录账本！")
            f.close()
        except IOError:
            print "open/write file error!"
if __name__=='__main__':
    rwer=RWer("1")
    rwer.save("2","2","2")
