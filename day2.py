# virtaulenv install 
# virtualenv <env-name>
# <env-name>/Scripts/activate

a = 1 + 2j
print(a)
print(type(a))


a = [0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,0]
print(a)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])

print(a[0::2])

print(a[-1])

print(a[-10:-3:2])

a = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]

# list functions 

a = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(a)

#len()

print(len(a))
a.append(10)
print(a)

a.extend([11, 12])
print(a)

a.insert(5, 100000000000000)
print(a)

# a.remove(100000000000000)
# print(a)

c = a.pop()
print(a)
print(c)

print(a.index(100000000000000))

a.sort(reverse=False)
print(a)

b = a.copy()

b[0] = 10000000000
print(b)
print(a)


# tuple


a = tuple()
a = (1, 2, 3, 4, 5, 6, 7)

#string 
a = "parv khush"
print(a[0])
print(a[4])

#dictionary
a = {
    "key": "value"
} 
a = dict({
    "key": "value"
})
print(a)


