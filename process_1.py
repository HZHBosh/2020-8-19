import multiprocessing
import time

def func():
    print("开始运行一个进程.....")
    time.sleep(2)
    print("结束进程!!!")

p=multiprocessing.Process(target=func)
p.start()

p.join()






