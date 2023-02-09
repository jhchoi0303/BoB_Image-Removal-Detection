import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from skimage.color import rgb2gray
import cv2 as cv
import os
import skimage #pip install scikit-image


def PCA_compress_image(path):
    pca = PCA(n_components=100) #n_components
    image = skimage.io.imread(path)
    image = rgb2gray(image)
    image_compressed = pca.fit_transform(image)
    img = pca.inverse_transform(image_compressed)
    filename = os.path.basename(path).split('/')[-1]
    cv.imwrite('./Output/PCA_'+filename, img)
