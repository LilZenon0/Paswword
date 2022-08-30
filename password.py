from collections import Counter

pin=input("input pin:")

list=[]

for i in range(len(pin)):
	a=int(pin[i])
	list.append(a)


dic=Counter(list)

times=10
print(dic,len(dic))

for i in range(1,len(dic)):
	times *=(10-i)
	


print(times)


