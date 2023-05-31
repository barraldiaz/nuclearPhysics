#/usr/bin/python3


from aux_functions import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import *



#We define the experimental counts
Nb=128919
Nbg=82357


#Files for the data

file_spectra="response_140Cs.rdm"
file_feed="Ib_140Cs.fed"



total_levels = 101

freq = []
effGB = []
effB = []
sFreq = []

for l in range(total_levels):

	
	
	
	freq.append(feed_level(file_feed,l)[0])
	sFreq.append(feed_level(file_feed,l)[1])	
	effGB.append(sum(spectra_sum(file_spectra,l)[1:]))	
	effB.append(sum(spectra_sum(file_spectra,l)[:]))
	if l == 100:
		continue
		


#We get coeficients

total_freq = sum(freq[1:])

effGB_tot_exc=0
effB_tot_exc=0	

for i in range(1,len(effGB)):
 	effGB_tot_exc = effGB_tot_exc + effGB[i]*freq[i]/total_freq
 	
for i in range(1,len(effB)):
 	effB_tot_exc = effB_tot_exc + effB[i]*freq[i]/total_freq

effGB_0=effGB[0]
effB_0=effB[0]



R = Nbg/Nb

c = effGB_0/effGB_tot_exc

a = effB_tot_exc/effGB_tot_exc

b=(effB_0-effB_tot_exc)/effGB_tot_exc



#Now once we have all coeficients we print

I_0 = (1-a*R)/(1+b*R-c)

#Now for uncertainy



sNb=859
sNbg=1667

num = (1-a*R)
den = (1+b*R-c)

sI0 = np.sqrt( ( (num*b/Nb-a*den/Nb) *sNbg/den**2)**2 +   ( (-b*Nbg*num/Nb**2+a*Nbg*den/Nb**2) *sNb/den**2)**2   )

print("=======================================================");print("")
print("The ground state intensity I0 is", str(I_0)[:6], "+-",str(sI0)[:6])
print("");print("=======================================================")




