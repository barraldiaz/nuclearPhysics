# nuclearPhysics
Programs related with nuclear physics

Here we will have some programs related to this field, to calibrate experiments, sustract noise, determination of some parameters etc


neutronPlasticDetector:
    program dedicated to the temperature and voltage calibration of a plastic neutron detector using gamma radiaiton from a 
    cesium 137 fount. It contains a program to obtain the middle drop point od the spectra, after this point should be kept and fitted on the 
    voltage.py and temperature.py to obtain the linear fit for the calibration
    
radiatorSubstract:
    program dedicated to the noise extraction and calibration of some detectors used in nuclear medical physics to study the secondary
    radiation in human tissues
    
betaDecayStudy:
    programs dedicated to the study of the beta decay, more precisely about the poblation of the ground state using the gamma-beta coincidence
    method. The runner.py runs the auxiliar functions and shows the I0 intensity to the ground state, also the other program will simulate different 
    populations of the excited states so we can see how this I0 intensity varies with this parameters.
    This ground state intensity is a very usefull parameter for nuclear reacions purposes, on nuclear reactors, yet also complicated
    due to the non gamma emision of this decay.
    
neutronPPAC:
    Programs used on my bachelor thesis dedicated to characterize a neutron detection system formed by 3 PPAC detectors used in GANIL SPIRAL2 
    experiment in France. Among others this programs filter the data, select the interest energy regions, reconstructs the beam, and obtain
    the efficiency varying with the neutron energy or angular dispersion.
    
