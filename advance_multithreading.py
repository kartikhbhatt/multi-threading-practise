# multithreading with threading pool
from concurrent.futures import ThreadPoolExecutor

def print_num(number):
    return f"Number: {number}"

numbers = [1,2,3,4,5]
if __name__=="__main__":

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_num,numbers)
    
    for result in results:
        print(result)