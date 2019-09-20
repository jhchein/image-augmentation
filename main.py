import os
import glob
from src.augment import Data_augmentation
from params import path, output_path, origin_filetype

os.makedirs(output_path, exist_ok=True)

origin_images = [f for f in glob.glob(f"{path}/*{origin_filetype}", recursive=True)]

print(path)
print(origin_images)

for full_filename in origin_images:
    print(full_filename)
    augmenter = Data_augmentation(full_filename)
    output_filename = augmenter.image_augment(save_path=output_path)
