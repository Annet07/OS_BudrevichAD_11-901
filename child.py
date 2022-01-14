#!/usr/bin/python3

import os
import random
import sys
import time

# Будревич Анна Дмитриевна, группа 11-901

args = sys.argv
if len(args) > 1:
    arg = int(args[1])
    pid = os.getpid()
    print(f"Запущена программа Child в процессе с PID {pid} с аргументом {arg}.")
    time.sleep(arg)
    status = random.randint(0, 1)
    os._exit(status)
else:
    print("Ошибка! Необходимо передать аргумент в дочерний процесс.")