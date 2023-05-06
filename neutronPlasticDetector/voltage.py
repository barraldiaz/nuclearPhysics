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



Verr=0.2
Terr=1



#First plot of T vs K:

fit, cov = np.polyfit(V, K , 1,cov=True)


Vfit=np.linspace(31,34,100)
Kfit=np.polyval(fit, Vfit)

uncer=np.sqrt(np.diag(cov))

r2 = np.corrcoef(V,K)[0,1]**2

print(r2)

legend= str(fit[1])[:6]+"+"+str(fit[0])[:5]+"* V \n "+ "$\pm$ (" + str(uncer[1])[:5] + ", " + str(uncer[0])[:5] + ") \n $r^2$ = " + str(r2)[:5]  
  


fig, ax = plt.subplots(figsize=(7,5))
ax.errorbar(V,K,yerr=Kerr, xerr=Verr, marker='o',linestyle='none',
    capsize=1.85,elinewidth=1.2, ms=5,mfc='white',mec='green',mew=1.2,ecolor='dimgrey', label=legend)
ax.plot(Vfit,Kfit,"k-")
ax.set_title("T = "+str(np.average(T))[:5])
ax.set_xlabel("Voltage (V)")
ax.set_ylabel("Coefficient K (A.U.)")
ax.legend(loc="best")

#Now to save it 
file_name= "vresults/"+pf+"_"+str(int(np.average(T)*10))+'.eps'
plt.savefig(file_name, format='eps')

plt.show()




