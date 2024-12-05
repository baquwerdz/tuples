tuples = (1,2,3,4,5)
print(tuples)
print(tuples[3])
#tuples[5] = 100
print(len(tuples))
del tuples
print("deleted")
#print(tuples)

adress = (12 , "street", "place", "country") #this is packing
for i in adress:
    print(i,end = "                                                 ")




# unpacking

housenumber, streetname, city, country = adress

print("-----------------------------------------------")
print("your house number is",housenumber )
print("your street name is",streetname )
print("your city is",city )
print("your country is",country )


print("-----------------------------------------------")

mytuple = 5, 4.6, "dog", "cat"
print(mytuple)

print("-----------------------------------------------")

NestedTuple = ("mouse", [1, 2, 3], (10, 20, 30))
print(NestedTuple [2][2])
print(NestedTuple [0])

print("-----------------------------------------------")

fruit = ["apple", "pear", "orange", "banana", "mango", "grape"]
print(fruit[2:5:1])
print(fruit[0:4:1])
