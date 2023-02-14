from Noise_Analysis import Noise_Analysis
from ELA import ELA
from Luminance_Gradient import Luminance_Gradient
from PCA import PCA_compress_image
import os
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider


def start():
    print("/$$$$$$$            /$$$$$$$     ")                                                                                                                                                                                          
    print("| $$__  $$          | $$__  $$   ")                                                                                                                                                                                         
    print("| $$  \ $$  /$$$$$$ | $$  \ $$   ")                                                                                                                                                                                           
    print("| $$$$$$$  /$$__  $$| $$$$$$$    ")                                                                                                                                                                                           
    print("| $$__  $$| $$  \ $$| $$__  $$   ")                                                                                                                                                                                           
    print("| $$  \ $$| $$  | $$| $$  \ $$   ")                                                                                                                                                                                           
    print("| $$$$$$$/|  $$$$$$/| $$$$$$$/   ")                                                                                                                                                                                           
    print("|_______/  \______/ |_______/    ")                                                                                                                                                                                           
    print("/$$$$$$                                                     /$$$$$$$                                                        /$$         /$$$$$$$              /$$                           /$$     /$$             ")       
    print("|_  $$_/                                                    | $$__  $$                                                      | $$        | $$__  $$            | $$                          | $$    |__/             ")      
    print("  | $$   /$$$$$$/$$$$   /$$$$$$   /$$$$$$   /$$$$$$         | $$  \ $$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$    /$$ /$$$$$$ | $$        | $$  \ $$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$$ /$$$$$$   /$$  /$$$$$$  /$$$$$$$ ")
    print("  | $$  | $$_  $$_  $$ |____  $$ /$$__  $$ /$$__  $$ /$$$$$$| $$$$$$$/ /$$__  $$| $$_  $$_  $$ /$$__  $$|  $$  /$$/|____  $$| $$ /$$$$$$| $$  | $$ /$$__  $$|_  $$_/   /$$__  $$ /$$_____/|_  $$_/  | $$ /$$__  $$| $$__  $$")
    print("  | $$  | $$ \ $$ \ $$  /$$$$$$$| $$  \ $$| $$$$$$$$|______/| $$__  $$| $$$$$$$$| $$ \ $$ \ $$| $$  \ $$ \  $$/$$/  /$$$$$$$| $$|______/| $$  | $$| $$$$$$$$  | $$    | $$$$$$$$| $$        | $$    | $$| $$  \ $$| $$  \ $$")
    print("  | $$  | $$ | $$ | $$ /$$__  $$| $$  | $$| $$_____/        | $$  \ $$| $$_____/| $$ | $$ | $$| $$  | $$  \  $$$/  /$$__  $$| $$        | $$  | $$| $$_____/  | $$ /$$| $$_____/| $$        | $$ /$$| $$| $$  | $$| $$  | $$")
    print(" /$$$$$$| $$ | $$ | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$        | $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$/   \  $/  |  $$$$$$$| $$        | $$$$$$$/|  $$$$$$$  |  $$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$")
    print("|______/|__/ |__/ |__/ \_______/ \____  $$ \_______/        |__/  |__/ \_______/|__/ |__/ |__/ \______/     \_/    \_______/|__/        |_______/  \_______/   \___/   \_______/ \_______/   \___/  |__/ \______/ |__/  |__/")
    print("                                 /$$  \ $$")                                                                                                                                                                                 
    print("                                |  $$$$$$/")                                                                                                                                                                                  
    print("                                 \______/")




start()
path = "../13/PIC 008.jpg"

Luminance_Gradient(path)



def update(val):
    sliderValue_ELA = ELA_Slider.val
    print(sliderValue_ELA)
    
    ELA(path,int(sliderValue_ELA))
    img1= plt.imread("./Output/ELA_"+filename)
    plt.subplot(2,3,1),plt.imshow(img1,cmap = 'gray')
    plt.title('ELA'), plt.xticks([]), plt.yticks([])
    
    sliderValue_NA = NA_Slider.val
    print(sliderValue_NA)
    
    Noise_Analysis(path, int(sliderValue_NA))
    img2= plt.imread("./Output/Noise_"+filename)
    plt.subplot(2,3,4),plt.imshow(img2,cmap = 'gray')
    plt.title('Noise-Analysis'), plt.xticks([]), plt.yticks([])

    
    sliderValue_PCA = PCA_Slider.val
    print(sliderValue_PCA)
    PCA_compress_image(path, int(sliderValue_PCA))
    img4= plt.imread("./Output/PCA_"+filename)
    plt.subplot(2,3,5),plt.imshow(img4,cmap = 'gray')
    plt.title('Principle Component Analysis'), plt.xticks([]), plt.yticks([])




filename = os.path.basename(path).split('/')[-1]

img1= plt.imread("./Output/ELA_"+filename)
plt.subplot(2,3,1),plt.imshow(img1,cmap = 'gray')
plt.title('ELA'), plt.xticks([]), plt.yticks([])


img2= plt.imread("./Output/Noise_"+filename)
plt.subplot(2,3,4),plt.imshow(img2,cmap = 'gray')
plt.title('Noise-Analysis'), plt.xticks([]), plt.yticks([])



img3= plt.imread("./Output/Luminance_"+filename)
plt.subplot(2,3,2),plt.imshow(img3,cmap = 'gray')
plt.title('Luminance-Gradient'), plt.xticks([]), plt.yticks([])



img4= plt.imread("./Output/PCA_"+filename)
plt.subplot(2,3,5),plt.imshow(img4,cmap = 'gray')
plt.title('Principle Component Analysis'), plt.xticks([]), plt.yticks([])



ELAx_Slider = plt.axes([0.75, 0.75, 0.2, 0.05])
ELA_Slider  = Slider(ELAx_Slider,'ELA slider', 0,100,  valinit=10)

ELA_Slider.on_changed(update)





NAx_Slider = plt.axes([0.75, 0.65, 0.2, 0.05])
NA_Slider  = Slider(NAx_Slider,'NA slider', 0,100,  valinit=20)

NA_Slider.on_changed(update)




PCAx_Slider = plt.axes([0.75, 0.6, 0.2, 0.05])
PCA_Slider  = Slider(PCAx_Slider,'PCA slider', 0,100,  valinit=10)
PCA_Slider.on_changed(update)


# img4= plt.imread("./Output/PCA_PIC 002.jpg")
# plt.subplot(2,3,3),plt.imshow(img4,cmap = 'gray')
# plt.title('Principle Component Analysis'), plt.xticks([]), plt.yticks([])


# img4= plt.imread("./Output/PCA_PIC 002.jpg")
# plt.subplot(2,3,6),plt.imshow(img4,cmap = 'gray')
# plt.title('Principle Component Analysis'), plt.xticks([]), plt.yticks([])

plt.show()