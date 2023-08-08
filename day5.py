# functions

# 25, 100000000

# def add_mul(a, b):
#     if (
#         (isinstance(a, int) or isinstance(a, float)) 
#         and
#         (isinstance(b, int) or isinstance(b, float))
#         ):
        
#         return a + b, a * b
#     return None
        
# def mul(a, b):
#     return a*b

    
# def main():
#     a, b = add_mul(2 , 1.1)
#     print(a, b)
    

# main()



def add(*args, **kwargs):
    ls = list([])
    for i in range(0, len(args) -1):
        # print(args[i], args[i+1])
        c = args[i] + args[i+1]
        ls.append(c)
        # print(c)
    return ls
    # return a+ b+ c


def another_main():
    ls = add(1, 1, 1, 1, 1, 1, 1, 1, this=11)
    print(ls)
    

if __name__ == "__main__":
    another_main()