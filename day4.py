## lksjdfl;

a = 0b00001111
print(bin(a))
print(a)
b = 5


# a = (1 << b)
a = ~(a)
print(a)
print(bin(a))
print(a)


# set bit 
a = 0b00001111
b = 5

a |= (1 << b)
print(a)

#unset bit
a = a & ~(1 << b)
print(a)

## loops 
 
i = 0
a = [12, 13, 54, 10, 5, 2]
while(i < len(a)):
    print(a[i])
    i+= 1
print()
print()
print()

for i in range(0, len(a)):
    if (a[i] == 54):
        print("heya")
        continue
    print(a[i])
print("f2lalsjdlf")       
        