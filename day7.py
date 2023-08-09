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
    
            
binary_search(14, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])