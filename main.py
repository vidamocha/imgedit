#!/usr/bin/env python3
"""
Simple Image Editor - Using only os and PIL (Pillow)
"""

import os
from PIL import Image, ImageFilter, ImageEnhance


def create_directories():
    """Create the necessary directories if they don't exist."""
    if not os.path.exists("images"):
        os.makedirs("images")
    if not os.path.exists("edited"):
        os.makedirs("edited")


def process_images():
    """Process all images in the images directory."""
    # Check if there are any images in the folder
    image_extensions = ('.JPG')
    images = []
    
    # List all image files in the images directory
    for file in os.listdir("images"):
        if file.lower().endswith(image_extensions):
            images.append(file)
    
    if not images:
        print("No images found in the 'images' directory!")
        print("Please add some images and run this script again.")
        return
    
    print(f"Found {len(images)} images to process.")
    
    # Process each image
    for image_file in images:
        input_path = os.path.join("images", image_file)
        
        # Create output filename
        file_name = os.path.splitext(image_file)[0]
        file_ext = os.path.splitext(image_file)[1]
        
        try:
            # Open the image
            with Image.open(input_path) as img:
                # Make different versions of the image
                
                # 1. Grayscale
                grayscale = img.convert("L")
                grayscale.save(os.path.join("edited", f"{file_name}_grayscale{file_ext}"))
                
                # 2. Blurred
                blurred = img.filter(ImageFilter.BLUR)
                blurred.save(os.path.join("edited", f"{file_name}_blurred{file_ext}"))
                
                # 3. Sharpened
                sharpened = img.filter(ImageFilter.SHARPEN)
                sharpened.save(os.path.join("edited", f"{file_name}_sharpened{file_ext}"))
                
                # 4. Enhanced brightness
                enhancer = ImageEnhance.Brightness(img)
                brightened = enhancer.enhance(1.5)  # Increase brightness by 50%
                brightened.save(os.path.join("edited", f"{file_name}_brightened{file_ext}"))
                
                # 5. Enhanced contrast
                enhancer = ImageEnhance.Contrast(img)
                contrasted = enhancer.enhance(1.5)  # Increase contrast by 50%
                contrasted.save(os.path.join("edited", f"{file_name}_contrasted{file_ext}"))
                
                # 6. Resized (half size)
                width, height = img.size
                resized = img.resize((width // 2, height // 2))
                resized.save(os.path.join("edited", f"{file_name}_resized{file_ext}"))
                
                # 7. Rotated
                rotated = img.rotate(90)
                rotated.save(os.path.join("edited", f"{file_name}_rotated{file_ext}"))
                
                print(f"Processed {image_file}: Created 7 edited versions")
                
        except Exception as e:
            print(f"Error processing {image_file}: {e}")


def main():
    """Main function to run the image editor."""
    print("Simple Image Editor")
    print("==================")
    
    # Create directories if they don't exist
    create_directories()
    
    # Process all images
    process_images()
    
    print("\nAll done! Check the 'edited' folder for the results.")


if __name__ == "__main__":
    main()
