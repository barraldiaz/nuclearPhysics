#/usr/bin/python3


from aux_functions import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import os
import time
def clear():
	os.system('clear')


I0 = []
reps=1000
start=float(time.time())
for i in range(reps):

	#feeding=create_random_levels(110)	
	feeding = create_random_levels_Ga(149)

	intensity=random_intensities(feeding)
	
	I0.append(intensity)
	
	if i%15==0 and i!=0:
		
		clear()
	
		print("");print("");print("===================================")
		print("time left to end: ", int((reps-i)*(time.time()-start)/i), " seconds ");print("")
		print("Iteration ", i, " of ", reps )
		print("===================================")

	
av, dev = np.mean(I0), np.std(I0)
text = "Average value is " + str(av)[:6] + " with \n deviation of " + str(dev)[:6]	
plt.hist(I0,bins=np.linspace(min(I0)-0.02,max(I0)+0.02,100), color='blue', label=text)
plt.legend(loc='best')
plt.xlabel("I0 Value")
plt.title("Descending gauss distribution \n  of feeding")
plt.ylabel("Counts")
plt.show()
