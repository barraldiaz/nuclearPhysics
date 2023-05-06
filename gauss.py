#!/usr/bin/python3



import matplotlib.pyplot as plt
import numpy as np
from sys import argv
import sympy as sp
import scipy.optimize as so

#We choose the file
file_name = argv[1]
end = int(argv[2])


#We extract the parameters from the name
#pf<photo number>_<voltage x 10>v_<temperature x 10>.bin
aux=file_name.split("_")
temperature=float(aux[2][:3])/10
voltage = float(aux[1][:3])/10


#We read the file
with open(file_name, "rb") as file:

	n_counts = np.fromfile(file, count = 1, dtype="int64")	
	energies= np.fromfile(file, dtype="float64", offset=64)
	


#=====================================================================================================================================================

def middle_point(x,y):
	#Se define la fuincion y los parametros iniciales aproximados:
	def ajuste(x,a,b,N):
		f= N*np.exp(-(x-a)**2/b)
		return f
	init_guess=[200.0,3,2]

	fit= so.curve_fit(ajuste, x , y , p0=(init_guess) ,absolute_sigma=False,method='trf',maxfev=10000000)
	ans=fit[0]; cov=fit[1]
	uncer=np.sqrt(np.diag(cov))

	#El termino fit[0] es un array con las soluciones:                               
	a,b, N = ans       
	    
	#Para las incertidumbres fit[1] es la matriz de covarianza por lo que:							
	sa,sb,sN = uncer
	    
	#Para graficar creamos puntos de nuestra funcion:
	xm=np.linspace(min(x)-min(x)/10,max(x)+max(x)/10,5000)
	ym=ajuste(xm,a,b,N)

	
	return a, sa, xm, ym


#We get position fo the max


#We make the fit to extract the values

h=np.histogram(energies, bins=np.linspace(0,end,end*100))

U0, sU, xm, ym = middle_point(h[1][1:],h[0][:])

#plt.plot(h[1],200/(np.exp((h[1]-4.8)/0.5)+1))

#We plot
plt.hist(energies, color="navy" ,  bins=np.linspace(0,end,end*100),histtype="step"  )
plt.plot(xm,ym, color='red', linewidth=1.1, label='Fit with U0=%1.3f $\pm$ %1.3f' % (U0, sU))
plt.ylabel("$ Counts $"); plt.xlabel("Energies (AU)")
plt.title("T=%1.1f  V=%1.1f" % (temperature, voltage) )
plt.legend(loc='upper right' )
save_name = "/home/angel/physics/pplab/graphs/"+file_name.split(".")[0].split("/")[1]+".eps"
plt.savefig(save_name, format="eps")
plt.show()










	
