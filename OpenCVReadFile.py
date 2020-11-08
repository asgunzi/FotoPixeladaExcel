# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:08:24 2020

@author: asgun
"""
import cv2
import csv

img = cv2.imread('C:\Analytics\klabin.jpg') #Mudar a origem da foto


#Mudar o endereço do arquivo CSV
with open('C:\Analytics\matrizKb.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ')
    
    for i in range(len(img[:])):
        spamwriter.writerow(img[i][:].flatten())
        