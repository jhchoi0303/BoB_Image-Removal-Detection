from Noise_Analysis import Noise_Analysis
from ELA import ELA
from Luminance_Gradient import Luminance_Gradient
from matplotlib import pyplot as plt

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
ELA("../13/PIC 002.jpg")
Noise_Analysis("../13/PIC 002.jpg")
Luminance_Gradient("../13/PIC 002.jpg")




img1= plt.imread("./Output/ELA_PIC 002.jpg")
plt.subplot(2,3,1),plt.imshow(img1,cmap = 'gray')
plt.title('ELA'), plt.xticks([]), plt.yticks([])


img2= plt.imread("./Output/Noise_PIC 002.jpg")
plt.subplot(2,3,4),plt.imshow(img2,cmap = 'gray')
plt.title('Noise-Analysis'), plt.xticks([]), plt.yticks([])



img3= plt.imread("./Output/Luminance_PIC 002.jpg")
plt.subplot(2,3,2),plt.imshow(img3,cmap = 'gray')
plt.title('Luminance-Gradient'), plt.xticks([]), plt.yticks([])

img3= plt.imread("./Output/Luminance_PIC 002.jpg")
plt.subplot(2,3,5),plt.imshow(img3,cmap = 'gray')
plt.title('Luminance-Gradient'), plt.xticks([]), plt.yticks([])


img3= plt.imread("./Output/Luminance_PIC 002.jpg")
plt.subplot(2,3,3),plt.imshow(img3,cmap = 'gray')
plt.title('Luminance-Gradient'), plt.xticks([]), plt.yticks([])


img3= plt.imread("./Output/Luminance_PIC 002.jpg")
plt.subplot(2,3,6),plt.imshow(img3,cmap = 'gray')
plt.title('Luminance-Gradient'), plt.xticks([]), plt.yticks([])



plt.show()