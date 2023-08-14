from day8 import time_calc
import time
import threading

from threading import Lock


# a = time.time()

# # @time_calc
# # def thread1():
# #     for _ in range(0, 100000000):
# #         pass
    
# @time_calc
# def thread1():
#     for _ in range(0, 100):
#         time.sleep(0.1)
    
# # @time_calc 
# # def thread2():
# #     for _ in range(0, 100000000):
# #         pass
   
# @time_calc 
# def thread2():
#     for _ in range(0, 100):
#         time.sleep(0.1)
    
# t1 = threading.Thread(target=thread1)
# t2 = threading.Thread(target=thread2)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# b = time.time()

# print(b-a)
count = 0

def inc(inc_by, lock):
    global count
    lock.acquire()
    temp_count = count 
    temp_count += inc_by
    time.sleep(0.2)
    count = temp_count
    lock.release()
    
lock = Lock()  
t1 = threading.Thread(target=inc, args=(10, lock,))
t2 = threading.Thread(target=inc, args=(20, lock,))

t1.start()
t2.start()

t1.join()
t2.join()

print(count)