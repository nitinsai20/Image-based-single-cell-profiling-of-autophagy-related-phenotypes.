# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:15:03 2022
@author: Nitin Beesabathuni
Detecting puncta and creating a mask using LoG and watershed programs. 
input is a array containing all the images for which you want to generate a puncta mask. 
output is also an array containing the labeled puncta mask for each image 
"""
import cv2 as cv
import numpy as np
from math import sqrt
from skimage.feature import blob_log
from skimage import segmentation, morphology
from scipy import ndimage as ndi

def puncta_mask(GFP_files_bg,threshold=0.0275,bitsize_8=True): 
    if bitsize_8 == True:
        #conversion of 16 bit to 8 bit float by dividing with 257(255/65537) after background subtraction if 8 bit is True
        GFP_files_bg= GFP_files_bg*255/65535
    
    #LoG (Laplacian of Gaussian) for detecting puncta with updated radius
    blobs_8bit= [] #defining a null list
    data= GFP_files_bg
    blobs_8bit.append(blob_log(data, min_sigma = 1, max_sigma=2, num_sigma=60, threshold=0.0275)) #change the threshold. 
    
    #generating a puncta mask for each image. 
    puncta_mask= np.zeros((2048,2048))
    
    #using cv2.circle for drawing puncta mask for each image. Followed by labeling using watershed. 
    img_circ=np.zeros((2048,2048))
    for pn in range(len(blobs_8bit[0])):
        y, x, r = blobs_8bit[0][pn]
        r= round(r* sqrt(2)) #radius calculations
        img_circ=cv.circle(img_circ, (int(x), int(y)),r,color=(255,0,255),thickness=-1)
    #labeling blobs by watershed. 
    distance= ndi.distance_transform_edt(img_circ)
    local_max=morphology.local_maxima(distance)
    markers=ndi.label(local_max)[0]
    puncta_mask= segmentation.watershed(img_circ,markers,mask=img_circ)
    return puncta_mask