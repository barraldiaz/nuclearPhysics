

#include <stdio.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <string>
#include <TString.h>
#include <algorithm>
#include <sstream>
#include <TROOT.h>
#include <TStyle.h>
#include <TFile.h>
#include <TObject.h>
#include <TTree.h>
#include <TCanvas.h>
#include <TMath.h>
#include <TGraph.h>
#include "TPad.h"
#include "TVirtualPad.h"
#include <iostream>

void noise_sustract(){

//To change from detector to another we need to change the nbins (31) and the parameters of the linear regresion to calibrate the energy

double energy;
double counts;

//Name of the fils with noise and data, and where to save it

char noise_file[30] = "DataR_run.root";
char data_file[30] = "DataR_run.root";
char save_file[30] = "processed_data.root";

//calibration parameters

double slope = 0.085114118;
double origin = -2.02468845;

//We read the raw file and we open it as a ttree
TFile *f1 = new TFile(data_file,"READ");
TTree *t1 = (TTree*)gDirectory->Get("Data_R;22");
t1->Draw("Energy>>h(16383,0,16383)","","goff"); //Here we should put the number of bins depending on our detector bits
TH1F *h = (TH1F*)gDirectory->Get("h");

//We asume we have 14 bits so 16384 bins

//We create the final histogram file to keep data:

  TAxis *axis1 = h->GetXaxis();
  int nbx=axis1->GetNbins();
  float xmin = axis1->GetXmin();
  float xmax = axis1->GetXmax();
  TH1F *hnew = new TH1F("counts","counts",nbx,xmin,xmax);
  
  for(int i=0;i<nbx;i++)
    {
      hnew->SetBinContent(i,h->GetBinContent(i)*nbx);      
    }
  
  //Now we have to open the noise file and substract it to our histogram data points:
  TFile *f2 = new TFile(noise_file,"READ");
  TTree *t2 = (TTree*)gDirectory->Get("Data_R;22"); 
  t2->Draw("Energy>>h2(16383,0,16383)","","goff");
  TH1F *h2 = (TH1F*)gDirectory->Get("h2");
  
  for(int i=0;i<nbx;i++)
    {
      hnew->SetBinContent(i,hnew->GetBinContent(i)-h2->GetBinContent(i)*nbx*0.5);      
    }
    
    
    //Now we create a root file and tree to get the final result:
    
    TFile *final_file = new TFile(save_file,"RECREATE"); 	
    TTree *data = new TTree("data","data");
    data->Branch("energy", &energy);
    data->Branch("counts", &counts);
   
    for(int i=0;i<nbx;i++)
    	{
    	counts = hnew->GetBinContent(i);
    	energy = hnew->GetBinCenter(i)*slope+origin;
    	data->Fill();
    	}    
    	
    final_file->Write();
    
    //Finally we can plot our file with the noise substracted
   
   TFile *visualize = new TFile(save_file,"READ");
   TTree *vis_data = (TTree *)gDirectory->Get("data");
   vis_data->Draw("counts:energy","","");
  
  
}
