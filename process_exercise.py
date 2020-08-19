import os
import multiprocessing
def getfile01():
    filename=open("dict.txt","rb")
    filename01=open("dict01.txt","wb")
    num = filesize // 2
    while num>1024:
        filename01.write(filename.read(1024))
        num -=1024
    filename01.write(filename.read(num))
    filename01.close()
    filename.close()
    print("dict01已写入......")


def getfile02():
    filename = open("dict.txt", "rb")
    filename02 = open("dict02.txt", "wb")
    num =filesize-(filesize // 2)
    filename.seek(num,0)
    while num>1024:
        filename02.write(filename.read(1024))
        num -=1024
    filename02.write(filename.read(num))
    filename02.close()
    filename.close()
    print("dict02已写入........")
filesize=os.path.getsize("dict.txt")


p1=multiprocessing.Process(target=getfile01)
p1.start()

p2=multiprocessing.Process(target=getfile02)
p2.start()

p1.join()
p2.join()



