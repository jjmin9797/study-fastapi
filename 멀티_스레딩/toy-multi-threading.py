import threading
import os
from concurrent.futures import ThreadPoolExecutor
import time


def one_time_bot(msg):
    print("Start One Time Bot!! : " + msg)
    print(f"PID : {os.getpid()} Process : {threading.get_ident()}")
    for i in range(1, 100):
        i + 1
    print("End One Time Bot!!")


def two_time_bot(msg):
    print("Start Two Time Bot!! :" + msg)
    print(f"PID : {os.getpid()} Process : {threading.get_ident()}")
    a = 0
    for i in range(1, 100000000):
        a += i
    print("End Two Time Bot!!")


def three_time_bot(msg):
    print("Start Three Time Bot!! : " + msg)
    print(f"PID : {os.getpid()} Process : {threading.get_ident()}")
    for i in range(1, 10000):
        i + 1
    print("End Three Time Bot!!")


def main():
    excutor = ThreadPoolExecutor(max_workers=5)
    msgs = [str(i) for i in range(1, 101)]
    excutor.map(two_time_bot, msgs)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Hello")
    print(f"걸린 시간 : {end - start}")
