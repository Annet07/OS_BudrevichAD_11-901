import sys
import os
import random
import time

#Будревич Анна Дмитриевна, группа 11-901

def run_program(n):
    for i in range(0, int(n)):
        pid = os.fork()
        if pid == 0:
            rand = random.randint(5, 10)
            sys.argv = ['parent.py', rand]
            exec(open("child.py").read())
        else:
            status = os.wait()
            print("Дочерний процесс с PID %d завершился. Статус завершения %d." % (pid, status[1] / 256))


if __name__ == '__main__':
    args = sys.argv
    run_program(args[1])

