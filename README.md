# Redis-poc
Redis未授权访问批量探测
（第一次自己写poc，纪念一下）
# 使用
```
   python Redis_poc.py -h
   
   
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
   
   
   usage: Redis_poc.py [-h] [--list LIST] [--lhost LHOST] [--lport LPORT] [--rhost RHOST] [--rport RPORT]
   
   Redis 未授权漏洞测试
   
   optional arguments:
     -h, --help     show this help message and exit
     --list LIST    输入批量文件路径，eag:target.txt
     --lhost LHOST  攻击机IP，eag: 127.0.0.1
     --lport LPORT  攻击机Port
     --rhost RHOST  目标IP
     --rport RPORT  目标端口
   
   
   ```
