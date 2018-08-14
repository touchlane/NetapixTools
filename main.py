from PIL import Image, ExifTags
import glob
import sys
import os


def rotate_image(filepath, outputpath, isPortrait):
    try:
        print(isPortrait)
        image = Image.open(filepath)
        print (image)
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                print("here")
                break
        exif = image._getexif()
        if exif:
            exif = dict(exif.items())
            if exif[orientation] == 1 and isPortrait == True:
                print("here1")
                image = image.rotate(90, expand=True)
            elif exif[orientation] == 6 and isPortrait == False:
                image = image.rotate(90, expand=True)
        image.save(outputpath + "/" + filepath.split("/")[-1])
        image.close()
    except (AttributeError, KeyError, IndexError):
        pass

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Some parameters missed! Try again.")
        sys.exit()
    images = glob.glob(os.path.abspath(sys.argv[1]) + '/*.JPG')
    outputpath = os.getcwd() + "/output"
    if not os.path.isdir(os.getcwd() + "/output"):
        os.makedirs(outputpath)
    if sys.argv[2].upper() == "PORTRAIT":
        for image in images:
            rotate_image(image, outputpath, True)
    elif sys.argv[2].upper() == "LANDSCAPE":
        for image in images:
            rotate_image(image, outputpath, False)

