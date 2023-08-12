# import time
# def time_calc(fun):
#     def wrapper(*args, **kwargs):
#         a = time.time()
#         res = fun()
#         b = time.time()
#         print(b - a)
#         return res
#     return wrapper

# @time_calc
# def main():
#     for i in range(0, 10):
#         time.sleep(1)
        
# main()


# class ClassName():
#     def __init__(self, a, b):
#         print("this method will be called")
#         self.a = a
#         self.b = b
    
        
#     def sum(self):
#         print(self.a)
#         print(self.b)
    
#     def __del__(self):
#         pass

# c = ClassName(a = 1000000, b = 20000000)
# c.sum()


# class Animal():
#     def __init__(self, name):
#         self.name = name
#     def speak(self, awaj=None):
#         return f"Animal speaks {awaj}" if awaj else "animal do not speak"
        
# class Kutru(Animal):
#     def __init__(self, breed, name):
#         super(Kutru, self).__init__(name)
#         self.breed = breed
        
#     def speak(self):
#         return super().speak("bhaw")
        
        
# class Biladu(Animal):
#     def __init__(self, color, name):
#         super().__init__(name)
#         self.color = color
        
#     def speak(self):
#         return super().speak("meao")   
        
        
# k = Kutru("desi", "dev")
# print(k.speak())
# print(k.__dict__)

# b = Biladu("blue", "tom")
# print(b.speak())


class A():
    class_a = 10
    
    def __init__(self):
        self.radius = 1
        self.a = 10
        self._a = 2
        self.__a = 3
        
    def __del__(self):
        print("destructor called")
    
    def method_a(self):
        print("method from A")
     
    @property   
    def rad(self):
        return self.radius
    
    @rad.setter   
    def rad_set(self, value):
        self.radius = value
       
    def __repr__(self):
        return f"A class with properties"
        
class B():
    def __init__(self):
        pass
    
    def method_b(self):
        print("method from b")
        
        
class C(A, B):
    def __init__(self):
        pass
    
    def method_c(self):
        print("method from c")
        
a = A()

print(a.a)       
print(a._a)  

a.rad_set = 10
print(a.rad)

           
c = C()
c.method_a()


