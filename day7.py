#decorators

# def fibo(range):
#     if range <= 1:
#         return range
#     return fibo(range-1) + fibo(range-2)

# n = 10
# a = 0
# b = 1

# for i in range(0, n):
    
#     c = (a+b)
#     print(c)
#     a = b
#     b = c
    
    
    
# def binary_search(ele, arr):
#     start_index = 0
#     end_index = len(arr) - 1
    
#     while (start_index != end_index and (start_index +1) != end_index):
#         if (ele == arr[(start_index+end_index) // 2]):
#             print("element {} at index {}".format(ele, (start_index+end_index) // 2))
#             break
#         elif (ele > arr[(start_index+end_index) // 2]):
#             start_index = (start_index+end_index) // 2
#         elif (ele < arr[(start_index+end_index) // 2]):
#             end_index = (start_index+end_index) // 2  
#     else:
#         print("element not found")        
    
            
# binary_search(14, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

# def custom_decorator(fun):
#     def wrapper(*args, **kwargs):
#         print("this are some task that should be taken care before execution")
#         result = fun(*args, **kwargs)
#         print(result)
#         print("this are some other tasks that should be executed after function completion")
#         return result
#     return wrapper

# @custom_decorator
# def sum(parv):
#     for i in range(0, parv):
#         yield (i + (i +1))
        
# a = sum(10)
# print(a)
# for i in a:
#     print(i)

def class_avg(__dict):
    avg = 0
    for i in __dict.values():
        avg += i
    avg = avg / len(__dict)
    print(avg)


num_of_students = int(input("Enter number of students: "))
dict_of_students = dict([])

for i in range(0, num_of_students):
    name = input(f"Enter name of student {i} and marks saparated with ' ' : ")
    a = name.split()
  
    dict_of_students.update({a[0]: int(a[1])})
    
class_avg(dict_of_students)
    