

from  concurrent.futures import ThreadPoolExecutor
from time import sleep
import random
import threading

def test_sleep():
    message = threading.currentThread().getName()
    print("Thread " + str(message) + " goes to sleep")
    r = random.random()
    t = r * 10
    sleep(t)
    print("Thread " + str(message) + " woke up and returns after " + str(t) + " seconds")

executor = ThreadPoolExecutor(max_workers=30)

for i in range(20):
    a = executor.submit(test_sleep)