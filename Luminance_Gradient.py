import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os

def Luminance_Gradient(path):
    name = path
    filename = os.path.basename(path).split('/')[-1]
    img = cv.imread(name,0)
    laplacian = cv.Laplacian(img,cv.CV_64F)
    sobelx = cv.Sobel(img, cv.CV_64F, 1,0, ksize=5)
    cv.imwrite('./Output/Luminance_'+filename, sobelx)
