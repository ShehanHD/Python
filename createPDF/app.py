import os
from PIL import Image


def create(imageList):
    img = []

    if len(imageList) is 0:
        print("Empty folder")
    else:
        for i in imageList:
            img.append(Image.open(r'Image/' + f'{i}').convert('RGB'))
        pdf = input("pdf file name you want to save(without .pdf)>")
        img[0].save(r'PDF/' + pdf + '.pdf', save_all=True, append_images=img)


path = input("Image folder>")

if os.path.exists(path):
    li = os.listdir(path)
    create(li)
else:
    print("Wrong folder")
