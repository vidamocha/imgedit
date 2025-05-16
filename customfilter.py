from PIL import Image
from main import pics_available, save_result
import os


def d_filter(img_f, img_name):
    '''Increase saturation of dark areas and increase saturation of bright areas'''
    adj_img = img_f.copy()
    rgb_vals = adj_img.load()
    width, height = adj_img.size #no brackets

    brightness_threshold = 150 #on a scale of 0-255

    for x in range(width):
        for y in range(height):
            red, green, blue = rgb_vals[x,y]
            pix_bright = (red+green+blue)/3
            if pix_bright> brightness_threshold:
                adj_factor = 1-0.25*((pix_bright-brightness_threshold)/105)
            else:
                adj_factor = 1+0.35*((brightness_threshold-pix_bright)/150)
            
            new_red = min(255,max(0,round(red*adj_factor)))
            new_green = min(255,max(0,round(green*adj_factor)))
            new_blue = min(255,max(0,round(blue*adj_factor)))
            rgb_vals[x,y] = (new_red, new_green, new_blue)
    
    save_result(adj_img, img_name, "d_filtered")


    
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
        d_filter(pic, selected)
        
    #    #print(image.size)
    #    pic.save("./edited/")
    #    passc