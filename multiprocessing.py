import time
from multiprocessing import Process

def cube():
    for i in range(5):
        time.sleep(1)
        print(f"cube {i} : {i*i*i}")
    return None
def square():
    for i in range(5):
        time.sleep(1)
        print(f"square {i} : {i*i}")
    return None


if __name__=="__main__":
    t1 = Process(target=cube)
    t2 = Process(target=square)
    t=time.time()

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    finished = time.time()-t

    print(f"finished time: {finished}")

