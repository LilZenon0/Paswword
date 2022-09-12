#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 22:04:32 2022

@author: ZenonHe
"""

from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm # recommended import according to the docs
import math
A=[]
B=[]


for i in range(1000000):
	A.append(f'{i:06}')
Times=[]
for i in range(1000000):
	Seclist=[]
	for j in range(0,6):
		a=int(A[i][j])
		Seclist.append(a)
	
	dic=Counter(Seclist)
	if len(dic)==1:
		Times.append(10)
	elif len(dic)==2:
		if (dic[0]== 0 and dic[7]!=0) or (dic[0]!=0 and dic[7]==0):
			Times.append(16)
		else:
			Times.append(58)
	elif len(dic)==3:
		if dic[0]!=0 and dic[7]!=0:
			Times.append(16)
		elif dic[0]== 0 and dic[7]==0:
			Times.append(336)
		else:
			Times.append(112)
	elif len(dic)==4:
		if dic[0]== 0 and dic[7]==0:
			Times.append(1680)
		elif dic[0]==1 and dic[7]==1:
			Times.append(112)
		else:
			Times.append(672)
	elif len(dic)==5:
		if dic[0]== 0 and dic[7]==0:
			Times.append(6720)
		if dic[0]!=0 and dic[7]!=0:
			Times.append(672)
		else:
			Times.append(3360)
	elif len(dic)==6:
		if dic[0]== 0 and dic[7]==0:
			Times.append(20160)
		if dic[0]!=0 and dic[7]!=0:
			Times.append(3360)
		else:
			Times.append(13440)


data=Times
print(Counter(data))
print(np.mean(data))
ecdf = sm.distributions.ECDF(data)

x = np.linspace(0, 100)

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
