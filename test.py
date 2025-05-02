import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter


def clean_file_name(pic_path):
    if not os.path.exists(pic_path):
        print("No pics? 🫵😂🫵")
        return 0
    for pic in os.listdir(pic_path):
        p_ext = Path(pic)
        p_ext.rename(p_ext.with_suffix)



def pics_available(folder_path):
    '''Make a list of available photos to edit'''
    file_list = []
    if not os.path.exists(folder_path):
        print("No pics? 🫵😂🫵")
        return []
    
    for pic in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, pic)):
            file_list.append(pic)

    return file_list


if __name__ == "__main__":
    proj_path = os.getcwd()
    originals_path = proj_path+"/images"
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