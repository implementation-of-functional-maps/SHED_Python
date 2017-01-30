# -*- coding:utf-8 -*-
import getpass
import sys
import telnetlib

HOST = "plata.ar.media.kyoto-u.ac.jp "
user = "katsurou" #raw_input("Enter your remote account: ")
password = "aniyamato" #getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.read_until('~$ ') # コマンドを実行する直前まで読み飛ばす
tn.write("ls\n")
result = tn.read_until('~$ ') # lsコマンド結果とゴミを格納
tn.write("exit\n")

tL = result.split("\n")[1:-1] # コマンドとプロンプトを削除
for line in tL:
    print(line)
