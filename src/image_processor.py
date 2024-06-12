from PIL import Image
from type.point import Point
import os
import numpy as np

# Global Variable
IMAGE_NAME = None
IMAGE_PATH = None
WIDTH = 0
HEIGHT = 0

def read_image() :
  global IMAGE_NAME
  global IMAGE_PATH
  global WIDTH
  global HEIGHT

  cwd = os.getcwd()
  test_dir = os.path.join(cwd, "test")
  is_valid = False

  while (not is_valid):
    try :
      print("Make sure to insert the image inside the /test folder.")
      filename = input("Insert the image filename: ")
      file_path = os.path.join(test_dir, filename)
      image = Image.open(file_path).convert('L')
      is_valid = True

      # Image brief data
      IMAGE_NAME = filename
      IMAGE_PATH = file_path
      WIDTH = image.size[0]
      HEIGHT = image.size[1]
      print(f"Image {filename} has the height of {HEIGHT}px and width of {WIDTH}px.")
      return image
    except:
      print("Image not found! Please make sure to enter a valid image filename.")


def manipulate_image(image, base_point: Point, encrypted_binary: str):
  pixel_values = list(image.getdata())
  start_height = base_point.y % HEIGHT
  start_width = base_point.x % WIDTH
  start_idx = (start_height * WIDTH)+ start_width

  binary_length = len(encrypted_binary)
  pixel_length = len(pixel_values)

  # print("Before Manipulation \n", pixel_values[start_idx: start_idx+binary_length])

  for i in range(binary_length):
    curr_bit = int(encrypted_binary[i])
    curr_px = int(pixel_values[(start_idx + i) % pixel_length])
    # Pixel Manipulation
    if (curr_bit == 1):
      new_curr_px = curr_px | 1
    else:
      new_curr_px = curr_px & ~1
    pixel_values[(start_idx + i) % pixel_length] = new_curr_px

  # print("After Manipulation \n", pixel_values[start_idx: start_idx+binary_length])

  # Make Image
  new_image = Image.new('L', (WIDTH, HEIGHT))
  new_image.putdata(pixel_values)
  return new_image
    

def save_image(image):
  cwd = os.getcwd()
  test_dir = os.path.join(cwd, "test")

  image_names = IMAGE_NAME.split(".")
  image_name = image_names[0]+"-enc"
  image_extension = image_names[1]

  result_image_name = image_name+"."+image_extension
  image.save(os.path.join(test_dir, result_image_name))
  print("Image has been saved inside the /test folder.")
  print("Encrypted image will have the tag \"-enc\".")

def search_image(image, base_point: Point, encrypted_length: int) -> str:
    pixel_values = list(image.getdata())
    start_height = base_point.y % HEIGHT
    start_width = base_point.x % WIDTH
    start_idx = (start_height * WIDTH)+ start_width

    pixel_length = len(pixel_values)
    result_binary = ""
    
    for i in range(encrypted_length):
      curr_px = int(pixel_values[(start_idx + i) % pixel_length])