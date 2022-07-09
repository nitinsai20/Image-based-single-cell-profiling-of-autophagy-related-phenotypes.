# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:43:44 2022

@author: Nitin Beesabathuni
This module is designed for correcting non unifrom illumination by subtracting background using rolling ball radius method. 
the main input is the image filename. 
The other input is the rolling ball radius which is used for estimating the background. Default is 200. 
the output is an array with subtracted background. 
"""
import numpy as np
from cellpose import io
from skimage import restoration

#imagepreprocessing- subtracting background. 
def rbs(GFP_filtered,radius=200):
    GFP_files_bg= np.zeros((2048,2048))
    img= io.imread(GFP_filtered)
    bg = restoration.rolling_ball(img, radius=radius)
    img_bg = img - bg
    GFP_files_bg= img_bg
    return GFP_files_bg
