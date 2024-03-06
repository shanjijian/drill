# 安装库：paramiko
# pip3 install paramiko

import time
import paramiko

class sshdrill:
    def __init__(self,args):
        self.host=args.host
        self.port=args.port
    def run(self,username,password):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=self.host, port=self.port, username=username, password=password)
            print("Success! Username:%s  Password:%s" % (username, password))
            time.sleep(0.5)
            exit(1)
        except Exception as e:
            print("Fail:%s  Username:%s  Password:%s" % (e, username, password))

        finally:
            ssh.close()