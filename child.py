import os
import random
import sys
import time

#Будревич Анна Дмитриевна, группа 11-901

def run_program(arg):
    pid = os.getpid()
    print("Запущена программа Child в процессе с PID %d с аргументом %d." % (pid, arg))
    time.sleep(arg)
    sys.exit(random.randint(0, 1))


if __name__ == '__main__':
    args = sys.argv
    n = int(args[1])
    run_program(n)