#!/usr/bin/python3

import sys
import os
import random

# Будревич Анна Дмитриевна, группа 11-901

args = sys.argv
if len(args) > 1:
    n = int(args[1])
    print(f"Запущен Parent.py с PID {os.getpid()} и аргументом {n}")
    pids = []
    for i in range(0, int(n)):
        pid = os.fork()
        if pid == 0:
            rand = str(random.randint(5, 10))
            os.execl("./Child.py", "Child.py", rand)
        else:
            pids.append(pid)

    while len(pids) > 0:
        child_pid, exit_status = os.wait()
        print(f"Дочерний процесс с PID {child_pid} завершился. Статус завершения {exit_status}.")
        pids.remove(child_pid)
else:
    print("Ошибка! Необходимо передать число дочерних процессов.")
    os._exit(1)

