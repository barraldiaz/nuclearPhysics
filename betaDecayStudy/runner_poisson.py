

from aux_functions import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import *


#we read the file with the counts

N = np.loadtxt("counts_62Ga_1e6.vec")
#Files for the data

file_spectra="response-62Ga.rdm"
file_feed="Ib_ensdf_62Ga.fed"

I_0vec = []
sI_0vec = []

for i in range(len(N[:,0])):
    total_levels = 148
    print("Column number ", i)
    Nbg= N[i,0]
    Nb= N[i,1]
    sNbg = np.sqrt(Nbg)
    sNb = np.sqrt(Nb)
    freq = []
    effGB = []
    effB = []
    sFreq = []
    print(sNbg,sNb)
    for l in range(total_levels):
    
        
        
        
        freq.append(feed_level(file_feed,l)[0])
        sFreq.append(feed_level(file_feed,l)[1])	
        effGB.append(sum(spectra_sum(file_spectra,l)[1:]))	
        effB.append(sum(spectra_sum(file_spectra,l)[:]))


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



    num = (1-a*R)
    den = (1+b*R-c)

    sI0 = np.sqrt( ( (num*b/Nb-a*den/Nb) *sNbg/den**2)**2 +   ( (-b*Nbg*num/Nb**2+a*Nbg*den/Nb**2) *sNb/den**2)**2   )


    print("=======================================================");print("")
    print("The ground state intensity I0 is", str(I_0)[:6], "+-",str(sI0)[:6])
    print("");print("=======================================================")

    I_0vec.append(I_0)
    sI_0vec.append(sI0)

    f = open("intensities2.txt", "a")
    f.write("{}\t{} \n ".format(I_0,sI0))
    f.close()   

fig, ax = plt.subplots(1,2, figsize = (13,6))
ax[0].plot(N[:,1],sI_0vec, 'ks' , label="Variation of I_0 \n with Nb/Nbg" )
ax[1].plot(N[:,1],I_0vec, 'ks',label="Variation of s(I_0) \n with Nb/Nbg")
ax[1].set_ylabel("I_0")
ax[1].set_xlabel("Nb")
ax[0].set_ylabel("s(I_0)")
ax[0].set_xlabel("Nb")
plt.savefig("plot.eps")
plt.show()





