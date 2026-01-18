import time 
from concurrent.futures import ProcessPoolExecutor

def get_squared(number):
    time.sleep(1)
    return f"S Number {number}: {number*number}"


numbers = [1,2,3,4,5,6,7]
if __name__=="__main__":
    t=time.time()
    with ProcessPoolExecutor(max_workers=3) as exec:
        results = exec.map(get_squared,numbers)
    
    finished=time.time()-t
    for result in results:
        print(result)
    print(finished)