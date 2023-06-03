import numpy as np
import matplotlib.pyplot as plt
from sys import argv


def spectra_level(file,selected_level):

	#We read the file
	data = np.loadtxt(file)

	#We get all the columns and separate by type
	eff_raw=data[:,2]
	levels_raw=data[:,1]
	bins_raw=data[:,0]


	#We create a level mask to select only the events of this level
	level_mask = (levels_raw==selected_level)

	#We apply the mask to raw vectors
	bins_masked = np.array(bins_raw[level_mask], dtype='int')
	eff_masked = eff_raw[level_mask]

	#We create the final arrays of efficiency and bins
	eff_final=np.zeros(int(max(bins_masked)+1), dtype='float')
	bins_final=np.arange(-0.5,max(bins_masked)+1.5,1)

	#We add the data for each bin center
	eff_final[bins_masked] = eff_masked[:]

	#We plot finally
	legend = "Spectra for excited state \n  number " + str(selected_level) 
	plt.stairs(eff_final[:],  bins_final[:]*40/1000, color='blue')
	plt.title(legend)
	plt.xlabel("E (MeV)")
	plt.ylabel("Normalised counts")
	plt.show()
	
	
	return eff_final
	
def spectra_sum(file,selected_level):

	#We read the file
	data = np.loadtxt(file)

	#We get all the columns and separate by type
	eff_raw=data[:,2]
	levels_raw=data[:,1]
	bins_raw=data[:,0]
	
	#We create a level mask to select only the events of this level
	level_mask = (levels_raw==selected_level)
	
	#We apply the mask and sum
	eff=eff_raw[level_mask]	

	return eff

def feed_level(file, level):
	#load the file
	data_feed = np.loadtxt(file)
	
	feed = data_feed[level,1]
	error_feed = data_feed[level,2]
	return feed, error_feed


def create_random_levels(N_levels):
	begin=100
	level_eff=[]
	for i in range(N_levels+1):
		eff = np.random.uniform(0,begin)
		level_eff.append(eff)
		begin=begin-eff	
	level_eff=np.array(level_eff)/100
	return level_eff
	
	
def create_random_levels_Ga(N_levels):
	begin=100
	level_eff=[]
	for i in range(N_levels+1):
		if i==0:
			eff = np.random.uniform(90,begin)
		else:
			eff = np.random.uniform(0,begin)
		level_eff.append(eff)
		begin=begin-eff	

	level_eff=np.array(level_eff)/100
	return level_eff
	
	


def random_intensities(beta_intensities):

	#We define the experimental counts
	Nb=207906
	Nbg=201672

	#Files for the data

	file_spectra="response-62Ga.rdm"
	file_feed="Ib_ensdf_62Ga.fed"



	total_levels = len(beta_intensities)

	freq = beta_intensities
	effGB = []
	effB = []

	for l in range(total_levels):
	
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


	return I_0

