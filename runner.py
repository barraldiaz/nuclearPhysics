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



'''
sFreq_total=sum(sFreq)
sigma_effGB2 = 0
sigma_effB2 = 0
for i in range(1,len(effGB)):
 	sigma_effGB2 = sigma_effGB2 + (effGB[i]*sFreq[i]/total_freq)**2+(effGB[i]*freq[i]*sFreq_total/total_freq**2)**2
 	
for i in range(1,len(effB)):
 	sigma_effB2 = sigma_effB2 + (effB[i]*sFreq[i]/total_freq)**2+(effB[i]*freq[i]*sFreq_total/total_freq**2)**2

sigma_effB=np.sqrt(sigma_effB2) 
sigma_effGB=np.sqrt(sigma_effGB2) 
#Coeficients uncertainy


sa=np.sqrt((sigma_effB/effGB_tot_exc)**2+(effB_tot_exc*sigma_effGB/effGB_tot_exc**2)**2)
sb=np.abs(effGB_0*sigma_effGB/effGB_tot_exc**2)
sc=np.sqrt((effB_0*sigma_effGB/effGB_tot_exc)**2+(sigma_effB/effGB_tot_exc)**2+(effB_tot_exc*sigma_effGB/effGB_tot_exc**2)**2)
sR=np.sqrt((sNbg/Nb)**2+(sNb*Nbg/Nb**2)**2)

#uncertainy of numerator and denominator
sUpper = np.sqrt((sa*R)**2+(a*sR)**2) 
sDowner = np.sqrt(sc**2+(sb*R)**2+(b*sR)**2)
 
Upper = 1-a*R
Downer = 1+b*R-c



#Final uncertainy
sI0=np.sqrt((sUpper/Downer)**2+(sDowner*Upper/Downer**2)**2)
'''


