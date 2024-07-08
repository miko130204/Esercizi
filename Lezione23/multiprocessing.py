import multiprocessing
import time

def sleep():
    print(f"sono nella funzione ")
    
    time.sleep(1)
    
    print(f"sto uscendo dalla funzione")
    

tic: float = time.time()

sleep()
sleep()

toc : float = time.time()
time_elapsed : float = toc - tic
print (f"{time_elapsed=}")