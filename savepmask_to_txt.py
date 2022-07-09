# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 10:34:52 2022
#saving puncta mask as text file. 
The inputs are punctamask as an array. the filname(fname) - same as the input filename. label- either GFP or TRITC and the path to store 
the txt files. 
@author: Nitin Beesabathuni]

"""
import numpy as np

def savepmask_to_txt(pmask,fname,label,path):
    char="\\"
    position=fname.rfind(char)-len(fname)+1
    fname=fname[position:-4]
    fname=label+'_'+fname
    floc=path+fname+".txt"
    np.savetxt(floc, pmask,fmt='%d')