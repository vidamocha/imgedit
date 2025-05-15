from PIL import Image
from main import pics_available, save_result
import os


def d_filter(img_f, img_name):
    adj_img = img_f
    rgb_vals = adj_img.load()
    width, height = adj_img.size()
    print(width, height)

if __name__ == "__main__":
    proj_path = os.getcwd()
    originals_path = proj_path+"/images"
    #clean_file_name(originals_path)
    available_pics = pics_available(originals_path)
    print(available_pics)

    proj_path = os.getcwd()
    originals_path = proj_path+"/images"
    #clean_file_name(originals_path)
    available_pics = pics_available(originals_path)

    selected = 0 

    while selected not in available_pics:
        for i in range(1,len(available_pics)+1):
            print(str(i)+")", available_pics[i-1])
        print("\n")
        selected = input("Which picture would you like to edit? \nType the name: \t") +".jpg"


    with Image.open(os.path.join(originals_path, selected)) as pic:
        print(pic.format, pic.size, pic.mode)
        
    #    #print(image.size)
    #    pic.save("./edited/")
    #    passc