from PIL import Image, ExifTags
import glob
import sys
import os


def rotate_image(filepath, outputpath):
    try:
        image = Image.open(filepath)
        print (image)
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                print("here")
                break
        exif = image._getexif()
        if exif:
            exif = dict(exif.items())
            print(exif[orientation])
            if exif[orientation] == 1:
                print("here1")
                image = image.rotate(90, expand=True)
            elif exif[orientation] == 6:
                print("here3")
                image = image.rotate(180, expand=True)
        image.save(outputpath + "/" + filepath.split("/")[-1])
        image.close()
    except (AttributeError, KeyError, IndexError):
        pass


if __name__ == '__main__':
    images = glob.glob(os.path.abspath(sys.argv[1]) + '/*.JPG')
    outputpath = os.getcwd() + "/output"
    if not os.path.isdir(os.getcwd() + "/output"):
        os.makedirs(outputpath)
    print(images)
    for image in images:
        rotate_image(image, outputpath)