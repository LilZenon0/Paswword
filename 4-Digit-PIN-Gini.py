#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 22:04:32 2022

@author: ZenonHe
"""

from collections import Counter
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


Get_items=Counter(Times)
Count_PIN=len(Times)

p=[]
i=0
for items in Get_items.keys():

	p.append((Get_items[items]/10000)**2)

print(p)	
p=sum(p)

Gini=1-p

print(Gini)


