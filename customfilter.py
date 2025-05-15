from main import pics_available
import os

proj_path = os.getcwd()
originals_path = proj_path+"/images"
#clean_file_name(originals_path)
available_pics = pics_available(originals_path)
print(available_pics)