#!/usr/bin/python3


import numpy as np

import matplotlib.pyplot as plt
from sys import argv

pf = str(argv[1])



data=np.loadtxt("data.txt")
	
	
	
#For U0 vs T:

V=data[:,0]
T=data[:,1]
K=data[:,2]
Kerr=data[:,3]*10

Verr=0.3
Terr=1



#First plot of T vs K:

fit, cov = np.polyfit(T, K , 1,cov=True)
uncer=np.sqrt(np.diag(cov))

Tfit=np.linspace(25,50,100)
Kfit=np.polyval(fit, Tfit)

r2 = np.corrcoef(T,K )[0,1]**2

legend= str(fit[1])[:6]+"+"+str(fit[0])[:5]+"* T \n "+ "$\pm$ (" + str(uncer[1])[:5] + ", " + str(uncer[0])[:5] + ") \n $r^2$ = " + str(r2)[:5]  

fig, ax = plt.subplots(figsize=(7,5))
ax.errorbar(T,K,yerr=Kerr, xerr=Terr, marker='o',linestyle='none',
    capsize=1.85,elinewidth=1.2, ms=5,mfc='white',mec='green',mew=1.2,ecolor='dimgrey', label=legend)
ax.plot(Tfit,Kfit,"k-")

ax.set_title("V = "+str(np.average(V))[:4])
ax.set_xlabel("Temperature (C)")
ax.set_ylabel("Coefficient K (A.U.)")
ax.legend(loc="best")

#Now to save it 
file_name= "tresults/"+pf+"_"+str(int(np.average(V)*10))+'.eps'
plt.savefig(file_name, format='eps')

plt.show()

