import os
from PIL import Image
from fpdf import FPDF

def create(imageList, path):
    img = []
    pdf = FPDF()

    if len(imageList) is 0:
        print("Empty folder")
    else:
        for image in imageList:
            pdf.add_page()
            width, height = Image.open(f'{path}/{image}').size
            pdf.image(f'{path}/{image}', 0, 0, float(width * 0.18), float(height * 0.18))

        #aaa = input("pdf file name you want to save(without .pdf)>")
        pdf.output('PDF/TPSI.pdf', "F")


path = input("Image folder>")

if os.path.exists(path):
    li = os.listdir(path)
    print(li)
    create(li, path)
else:
    print("Wrong folder")

