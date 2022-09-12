from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm # recommended import according to the docs
import math
A=[]
B=[]


for i in range(10000):
	A.append(f'{i:04}')
Times=[]
for i in range(10000):
	Seclist=[]
	for j in range(0,4):
		a=int(A[i][j])
		Seclist.append(a)
	
	dic=Counter(Seclist)
	if len(dic)==1:
		Times.append(math.log2(10)*4)
	elif len(dic)==2:
		if (dic[0]== 0 and dic[7]!=0) or (dic[0]!=0 and dic[7]==0):
			Times.append(math.log2(16)*4)
		else:
			Times.append(math.log2(58)*4)
	elif len(dic)==3:
		if dic[0]!=0 and dic[7]!=0:
			Times.append(math.log2(16)*4)
		elif dic[0]== 0 and dic[7]==0:
			Times.append(math.log2(336)*4)
		else:
			Times.append(math,log2(112)*4)
	elif len(dic)==4:
		if dic[0]== 0 and dic[7]==0:
			Times.append(math.log2(1680)*4)
		elif dic[0]==1 and dic[7]==1:
			Times.append(math.log2(112)*4)
		else:
			Times.append(math.log2(672)*4)         



data=Times
print(Counter(data))
print(np.mean(data))
ecdf = sm.distributions.ECDF(data)

x = np.linspace(min(data),max(data))

y = ecdf(x)



plt.xlabel("Entropy(bits)")

plt.ylabel("Eempirical CDF")

plt.step(x, y)

plt.show()

fig,ax0 = plt.subplots(nrows=1,figsize=(6,6))
#第二个参数是柱子宽一些还是窄一些，越大越窄越密
ax0.hist(data,10,density=0.1,histtype='bar',facecolor='yellowgreen',alpha=0.75)
	#times=10

	#for i in range(1,len(dic)):
		#times *=(10-i)
	
	#Times.append(math.log2(times)*4)




