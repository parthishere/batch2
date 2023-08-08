#functions 


# def func(a, b=0):
#     print(a, b)
    
# func(1, 5)
# n = 4
# fact = 1
# while (n > 1):
#     fact = fact * n 
#     n -= 1

# print(fact)

def factorial(num=5):
    if (num <= 1):
        return 1
    c = factorial(num-1)*num
    return c
    
print(factorial())
