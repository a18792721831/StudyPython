from PIL import Image
import os


def webp2Jpg(sourceFile):
    image = Image.open(sourceFile)
    image.load()
    image.save(sourceFile.replace('.webp', '.jpg'), 'JPEG')
    os.remove(sourceFile)
