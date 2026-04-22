import os
os.system("clear")

tuple1 = ("salom", 'hello', 13, 5.5, True)

# tuple1[3] = 777.   tupleni o'zgartirib bolmaydi

print(tuple1)
print(tuple1[1])

tuple2 = (44, 11, 33, 22, 55, 99, 77, 88, 111, 130, 120)

print(tuple2)
print(tuple2[3])
print(tuple2[2:7])
print(tuple2[:5])
print(tuple2[3:])
print(tuple2[2:9:2])
print(tuple2[-1])
#print(tuple2[99])
print(tuple2[::-1])
print(sorted(tuple2))