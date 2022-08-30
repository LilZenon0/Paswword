from collections import Counter
import matplotlib.pyplot as plt
import matplotlib as mt
import plotly
import pandas as pd
#from mayavi import mlab
A=[]



for i in range(100):
	A.append(f'{i:04}')
Times=[]
for i in range(100):
	Seclist=[]
	for j in range(0,4):
		a=int(A[i][j])
		Seclist.append(a)
	
	dic=Counter(Seclist)

	times=10

	for i in range(1,len(dic)):
		times *=(10-i)
	
	Times.append(times)


plt.hist(self,Times,'step')

plt.show()
#res={'Password':A,'Times':Times}
#dif=pd.DataFrame(data=res,columns=['Password','Times'])
#fig=px.scatter(dif,x="Password",y="Times")

#plotly.offline.plot(fig)