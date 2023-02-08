from wand.image import Image #https://imagemagick.org/script/download.php#windows #pip install wand #https://www.geeksforgeeks.org/python-noise-function-in-wand/
import os

def Noise_Analysis(path):
    filename = path
    name = os.path.basename(path).split('/')[-1]
    with Image(filename = filename) as img:
        img.noise("laplacian", attenuate = 10.0)
        img.save(filename= './Output/Noise_'+name)