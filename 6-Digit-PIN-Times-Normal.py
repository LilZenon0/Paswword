#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 22:04:32 2022

@author: ZenonHe
"""


from collections import Counter
import numpy as np

A=[]



for i in range(1000000):
	A.append(f'{i:06}')
Times=[]
for i in range(1000000):
	Seclist=[]
	for j in range(0,6):
		a=int(A[i][j])
		Seclist.append(a)
	
	dic=Counter(Seclist)

	times=10

	for i in range(1,len(dic)):
		times *=(10-i)
	
	Times.append(times)

print(np.mean(Times))
