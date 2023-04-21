from PIL import Image
import os

datasetpath = "pngsDataset/"
resultspath = "images_croped/"

fg_folders = [
    ("CocaCola/"),
    ("TimHortons/"),
    ("Pringles/"),
    ("Zucaritas/"),
    ("Lysol/"),
    ("Destop/")
]

for folder in fg_folders:
    for filename in os.listdir(f"{datasetpath}{folder}"):
        try:
            myImage = Image.open(datasetpath+folder+filename)
            black = Image.new('RGBA', myImage.size)
            myImage = Image.composite(myImage, black, myImage)
            myCroppedImage = myImage.crop(myImage.getbbox())
            myCroppedImage.save(f"{resultspath}{folder}{filename}")
        except:
            continue

