## file handling 
# lent = None
# with open("bhulo bhale biju badhu maa baap ne bhulsho nai.txt", "r") as file:
#     lent = file.readlines()
    
# with open("bhulo bhale biju badhu maa baap ne bhulsho nai.txt", "r") as file:
#     total = []
#     for i in range(0, len(lent)):
#         try:
#             ls = int(file.readline().split("->")[0])
#             total.append(ls)
            
#         except ValueError:
#             print("Value error occured")
        
        
#     print((sum(total) - 40) / 20)
    
## classes

# class AdvanceDict(dict):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
        
        
        
      
# c = ()
# class ComplexNumber():
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
#     def __add__(self, other):
#         if other.__class__ != self.__class__:
#             raise SyntaxError
#         else:
#             real = self.real + other.real
#             img = self.img + other.img
#             print(real, img)

#     def __mul__(self, other):
#         if type(other) == type(self):
#             pass
        
    
# a = ComplexNumber(1, 3)
# b = ComplexNumber(1, 4)
# a + b
# a * b


# a = [1, 2, 3]
# b = [1, 2, 4]
# a+ b
# 2, 7


## threading

# while True:
#     print("Hello world")
from day8 import time_calc
import time

a = time.time()

# @time_calc
# def thread1():
#     for _ in range(0, 100000000):
#         pass
    
@time_calc
def thread1():
    for _ in range(0, 100):
        time.sleep(0.1)
    
# @time_calc 
# def thread2():
#     for _ in range(0, 100000000):
#         pass
   
@time_calc 
def thread2():
    for _ in range(0, 100):
        time.sleep(0.1)
    
thread1()
thread2()
b = time.time()

print(b-a)
# Django intro

