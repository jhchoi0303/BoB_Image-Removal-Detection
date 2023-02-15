from wand.image import Image 
import os

def Noise_Analysis(path, degree):
    filename = path
    name = os.path.basename(path).split('/')[-1]
    with Image(filename = filename) as img:
        img.noise("laplacian", attenuate = degree)
        img.save(filename= './Output/Noise_'+name)