import os, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageOps
import math


def clean_file_name(pic_path):
    if not os.path.exists(pic_path):
        print("No pics? 🫵😂🫵")
        return 0
    for pic in os.listdir(pic_path):
        file_path = Path(os.path.join(pic_path, pic))
        if file_path.is_file():
            old_ext= file_path.suffix
            lower_ext = old_ext.lower()

            if old_ext!= lower_ext:
                new_file_name = file_path.stem + lower_ext
                new_file_path = file_path.with_name(new_file_name)

                file_path.rename(new_file_path)
                print("File extensions have now been standardized")
            else:
                print("All extensions were fomatted")
    


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

def open_img(folder_path):
    pass


def save_result(img, orig_name, eff_name="edited", output_dir="edited"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    base_name = os.path.splitext(os.path.basename(orig_name))[0]
    extension = os.path.splitext(os.path.basename(orig_name))[1]

    new_file_name = f"{base_name}_{eff_name}{extension}"
    output_path = os.path.join(output_dir, new_file_name)

    img.save(output_path)
    return output_path


def grey_scale(colour_img, orig_name):
    grey_scale_img = colour_img.convert("L")
    save_result(grey_scale_img, orig_name, "greyscale")
    return 0

def color_gain(original_img, orig_name):
    adjusted_image = original_img
    rgb_vals = adjusted_image.load()
    width, height = adjusted_image.size

    red_adj = int(input("Would you like to boost (1) or washout (-1) the reds: "))
    blue_adj = int(input("Would you like to boost (1) or washout (-1) the blues: "))
    green_adj = int(input("Would you like to boost (1) or washout (-1) the greens: "))

    for x in range(width):
        for y in range(height):
            red, blue, green = rgb_vals[x,y]
            red = min(255, max(0,red+red_adj))
            blue = min(255, max(0,blue+blue_adj))
            green = min(255, max(0,green+green_adj))
            rgb_vals[x,y] = (red, blue, green)

    #adjusted_colours = original_img
    save_result(adjusted_image, orig_name, "colour_gain" )
    #return adjusted_image

def apply_basic_filters(img):
    filters = {
        "blur": img.filter(ImageFilter.BLUR),
        "contour": img.filter(ImageFilter.CONTOUR),
        "detail": img.filter(ImageFilter.DETAIL),
        "edge_enhance": img.filter(ImageFilter.EDGE_ENHANCE),
        "emboss": img.filter(ImageFilter.EMBOSS),
        "find_edges": img.filter(ImageFilter.FIND_EDGES),
        "sharpen": img.filter(ImageFilter.SHARPEN),
        "smooth": img.filter(ImageFilter.SMOOTH)
    }
    return filters


def apply_elliptical_vignette(img, orig_name, strength=2.5):
    if img.mode != "RGB":
        img = img.convert("RGB")

    width, height = img.size
    center_x = width / 2
    center_y = height / 2

    vignette = Image.new("L", (width, height))
    pixels = vignette.load()

    for y in range(height):
        for x in range(width):
            dx = (x - center_x) / (width / 2)
            dy = (y - center_y) / (height / 2)
            distance = math.sqrt(dx ** 2 + dy ** 2)

            # Scale the darkening effect
            darkening = distance ** strength
            pixel_val = int((1 - min(1, darkening)) * 255)
            pixels[x, y] = pixel_val

    vignette_mask = Image.merge("RGB", (vignette, vignette, vignette))
    result = ImageChops.multiply(img, vignette_mask)
    save_result(result, orig_name, "vignette" )
    return result



if __name__ == "__main__":
    proj_path = os.getcwd()
    originals_path = proj_path+"/images"
    clean_file_name(originals_path)
    available_pics = pics_available(originals_path)

    selected = 0 

    while selected not in available_pics:
        for i in range(1,len(available_pics)+1):
            print(str(i)+")", available_pics[i-1])
        print("\n")
        selected = input("Which picture would you like to edit? \nType the name: \t") +".jpg"


    with Image.open(os.path.join(originals_path, selected)) as pic1:
        pic = pic1
        print(pic.format, pic.size, pic.mode)

        grey_scale(pic,selected)

        color_gain(pic, selected)

        apply_elliptical_vignette(pic, selected)
        
        



        filtered_versions = apply_basic_filters(pic)
        for name, filtered_img in filtered_versions.items():
            save_result(filtered_img, selected, eff_name=name)
    #    #print(image.size)
    #    pic.save("./edited/")
    #    passc