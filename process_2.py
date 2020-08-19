import multiprocessing
import time
def worker(sec,name,age):
    for i in range(3):
        time.sleep(sec)
        print(f"我叫{name}")
        print(f"我{age}岁了")
p=multiprocessing.Process(target=worker,
                          args=(1,"James"),
                          kwargs={"age":18})
p.start()
p.join()

print("结束父进程！！！！")

