#15.1 Use multiprocessing to create three separate processes. 
#Make each one wait a random number of seconds between zero and one, 
#print the current time, and then exit.

import multiprocessing
import random
import time

def whoami(message):
    time.sleep(random.uniform(0, 1))
    print(message)
    print("Current time:", time.ctime())

if __name__ == "__main__":
    processes = []

    for n in range(3):
        p = multiprocessing.Process(target=whoami,
                                    args=(f"I'm function {n}",))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()