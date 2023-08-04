### dict.


a = dict({
    "key":"value",
    "key2":"value2",
    "key3":"value3",
})

print(a)

# a.clear()
#  
b = a.copy()
print(b)

a = {}
list1 = ["key1", "key2", "key3"]
value = "random"
a = a.fromkeys(list1, value)
print(a)

print(a["key1"])
a["key1"] = "random2"
a["key5"] = 5
print(a)

a.update({"key2":2})
a.update({"key6":6})
print(a)

### 

print(a.keys())
print(a.values())
print(a.items())


## 

c = a.pop("key2")
print(c)
print(a)
a.popitem()
print(a)

############################3333
#sets()



a = {1, 2, 3, 3, 4, 5, 6}
a = set([1 ,2, 3, 3, 4, 5, 6, 7])
b = set([ 5, 6, 7, 8, 9, 10])
print(a)

a.add(8)
print(a)

# a.difference_update(b)
# print(a)


# print(a.intersection(b))

print(a.union(b))




######################
a = "thAkkAr pArTh"
print(a.upper())
print(a.lower())
print(a.title())
print(a.swapcase())
print(a.capitalize())
print(a.casefold())
print(a.center(15, "*"))
print(a.rjust(15, "*"))

# b = a.strip("p")
# print(b)
print(a.find("pArTh"))
print(a.replace("pArTh", "parth"))

## string.startswith(prefix, startindex, endindex)

# print(a.upper())
# print(a.upper())
# print(a.upper())
