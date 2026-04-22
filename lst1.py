lst1 = [1,2,3,4,"Salom", "Hello"]
lst1[3] = "Good"
print(lst1)
print(lst1[1])

# metod 

lst2 = (1,2,3,4,"Salom", "Hello", 2,3,4,2,3,2)

print(lst2.index("Salom"))

print(lst2.count(4))


t1 = (1,2,3,7,4,2,3,2,1,4,5,6,3,4,3)
print(max(t1, key=t1.count))