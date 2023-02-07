from PIL import Image, ImageChops, ImageEnhance
#from wand.image import Image #https://imagemagick.org/script/download.php#windows #pip install wand #https://www.geeksforgeeks.org/python-noise-function-in-wand/

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

#ELA conversion   
def convert_to_ela_image(path, quality):
    filename = path
    resaved_filename = filename.split('.')[0] + '.resaved.jpg'
    im = Image.open(filename).convert('RGB')
    im.save(resaved_filename, 'JPEG', quality=quality)
    resaved_im = Image.open(resaved_filename)
    
    ela_im = ImageChops.difference(im, resaved_im)
    
    extrema = ela_im.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1
    scale = 255.0 / max_diff
    ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)
    
    return ela_im

def ELA(path):
    new_filename=path.split('.')[0] + '.ELA.jpg'
    img = convert_to_ela_image(path, 1) 
    img.save(new_filename,'JPEG', quality = 100); #ELA
    
def Noise_Analysis(path):
     new_filename=path.split('.')[0] + '.Noise.jpg'
     with Image(filename =path) as img:
       img.noise("laplacian", attenuate = 1.0)
       img.save(filename = new_filename)





start()
ELA("./13/PIC 002.jpg")
Noise_Analysis("./13/PIC 002.jpg")