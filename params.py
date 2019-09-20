import os

path = os.path.join(os.getcwd(), "data")
output_path = os.path.join(path, "output")

origin_filetype = "bmp"
target_filetype = "jpg"

vflip_probability = .5
hflip_probability = .5
random_angle_range = (0, 90)
zoom_range = (0.95, 1.05)
