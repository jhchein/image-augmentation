import os
import glob
from augment import Data_augmentation

path = "C:\\Users\\hehein\\Downloads\\"
output_path = os.path.join(path, "output")
os.makedirs(output_path, exist_ok=True)
origin_filetype = ".jpg"

origin_images = [f for f in glob.glob(f"{path}/*{origin_filetype}", recursive=True)]

print(path)
print(origin_images)

for full_filename in origin_images:
    print(full_filename)
    augmenter = Data_augmentation(full_filename)
    output_filename = augmenter.image_augment(save_path=output_path)
