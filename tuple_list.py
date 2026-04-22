tuple1 = ('olma', 'anor', 'gilos', 'banan')

for i in tuple1:
    print(i)



# tuple1 = ('olma', 'anor', 'gilos', 'banan', 'uzum',)
# tuple2 = ('ALi', 'Vali', 'Xasan', 'Xusan')
# tuple3 = tuple1 + tuple2
# print(tuple3)

sonlar = (1,2,3,4,5,6,7,8,9)
# a = sonlar[0]
# b = sonlar[1]
# c = sonlar[2]
a,b,*c = sonlar
print(a,b,c)

print(len(sonlar))