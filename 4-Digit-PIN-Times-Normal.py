from collections import Counter
import numpy as np

A=[]



for i in range(10000):
	A.append(f'{i:04}')
Times=[]
for i in range(10000):
	Seclist=[]
	for j in range(0,4):
		a=int(A[i][j])
		Seclist.append(a)
	
	dic=Counter(Seclist)

	times=10

	for i in range(1,len(dic)):
		times *=(10-i)
	
	Times.append(times)

print(np.mean(Times))


