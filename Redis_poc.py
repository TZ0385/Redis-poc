'''
1、导入redis模块，用来执行redis命令
2、连接待测地址，如果返回信息，则存在未授权
3、地址参数采用手动输入获取
'''
import redis
from argparse import ArgumentParser


class Redis:
    def __init__(self):
        pass

    def connect(self, rhost):
        ip = rhost
        try:

            r = redis.StrictRedis(host=ip, port=result.rport)
            r.info()
        except:
            print("目标%s不存在未授权访问漏洞！" % result.rhost)
            return False
        else:
            print("目标%s存在未授权漏洞！！！" % result.rhost)
            print(r.info())

    def check(self):
        if result.list:
            with open(result.list, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    ip = line.strip()
                    poc(ip)
        else:
            poc(result.rhost)


def poc(rhost):
    ip = rhost
    try:

        r = redis.StrictRedis(host=ip, port=result.rport)
        r.info()
    except:
        print("目标%s不存在未授权访问漏洞！" % result.rhost)
        return False
    else:
        print("[漏洞告警]--目标 %s 存在未授权漏洞！！！" % result.rhost)



if __name__ == '__main__':
    show = '''
    
 /$$$$$$$                  /$$ /$$                                              
| $$__  $$                | $$|__/                                              
| $$  \ $$  /$$$$$$   /$$$$$$$ /$$  /$$$$$$$        /$$$$$$   /$$$$$$   /$$$$$$$
| $$$$$$$/ /$$__  $$ /$$__  $$| $$ /$$_____/       /$$__  $$ /$$__  $$ /$$_____/
| $$__  $$| $$$$$$$$| $$  | $$| $$|  $$$$$$       | $$  \ $$| $$  \ $$| $$      
| $$  \ $$| $$_____/| $$  | $$| $$ \____  $$      | $$  | $$| $$  | $$| $$      
| $$  | $$|  $$$$$$$|  $$$$$$$| $$ /$$$$$$$/      | $$$$$$$/|  $$$$$$/|  $$$$$$$
|__/  |__/ \_______/ \_______/|__/|_______/       | $$____/  \______/  \_______/
                                                  | $$                          
                                                  | $$                          
                                                  |__/                          
                                                                    By DA
    '''
    print(show + '\n')
    arg = ArgumentParser(description="Redis 未授权漏洞测试")
    arg.add_argument('--list', help='输入批量文件路径，eag:target.txt', dest='list')
    arg.add_argument('--lhost', help='攻击机IP，eag: 127.0.0.1')
    arg.add_argument('--lport', help='攻击机Port')
    arg.add_argument('--rhost', help='目标IP')
    arg.add_argument('--rport', help='目标端口', default=6379)
    result = arg.parse_args()
    Redis().check()
