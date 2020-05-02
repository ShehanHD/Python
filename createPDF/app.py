import os
import img2pdf
from PIL import Image
from time import sleep

def create(imageList, path):
    img = []

    if len(imageList) is 0:
        print("Empty folder")
    else:
        for i in imageList:
            img.append(Image.open(r''+path+'/' + f'{i}').convert('RGB'))
            sleep(1)
        pdf = input("pdf file name you want to save(without .pdf)>")
        img[0].save(r'PDF/' + pdf + '.pdf', save_all=True, append_images=img)


path = input("Image folder>")

if os.path.exists(path):
    li = os.listdir(path)
    create(li, path)
else:
    print("Wrong folder")


#1152x1535