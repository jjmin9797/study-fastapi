import time
import os
import threading

nums = [50, 63, 32]


def cpu_bound_func(num):
    print(f"PID : {os.getpid()} PROCESS : {threading.get_ident()} -> THREAD")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():
    result = [cpu_bound_func(num) for num in nums]
    print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("걸린 시간 : ", end - start)
