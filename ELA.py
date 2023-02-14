from PIL import Image, ImageChops, ImageEnhance
import os


def convert_to_ela_image(path, degree):
    filename = path
    resaved_filename = filename.split('/')[-1] + '.resaved.jpg'
    im = Image.open(filename).convert('RGB')
    
    print(degree)

    im.save(resaved_filename, 'JPEG', quality=degree)
    resaved_im = Image.open(resaved_filename)
    
    ela_im = ImageChops.difference(im, resaved_im)
    
    extrema = ela_im.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1
    scale = 255.0 / max_diff
    ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)
    
    return ela_im

def ELA(path, scale):
    name = os.path.basename(path).split('/')[-1]
    degree = scale
    img = convert_to_ela_image(path, degree)  #두번쨰인자조정
    img.save('./Output/ELA_'+name, quality = 100)