import random
import os
import glob
import cv2

from params import vflip_probability, hflip_probability, random_angle_range, zoom_range, origin_filetype, target_filetype

class Data_augmentation:
    def __init__(self, full_filename):
        '''
        Import image
        :param path: Path to the image
        :param image_name: image name
        '''
        self.path, self.filename = os.path.split(full_filename)
        self.name, self.extension = os.path.splitext(self.filename)
        self.image = cv2.imread(full_filename)

        # self.gaussian_noise_probability = .2

    def rotate(self, image, angle=90, scale=1.0):
        '''
        Rotate the image
        :param image: image to be processed
        :param angle: Rotation angle in degrees. Positive values mean counter-clockwise rotation (the coordinate origin is assumed to be the top-left corner).
        :param scale: Isotropic scale factor.
        '''
        w = image.shape[1]
        h = image.shape[0]
        #rotate matrix
        M = cv2.getRotationMatrix2D((w/2,h/2), angle, scale)
        #rotate
        image = cv2.warpAffine(image,M,(w,h))
        return image

    def flip(self, image, vflip=False, hflip=False):
        '''
        Flip the image
        :param image: image to be processed
        :param vflip: whether to flip the image vertically
        :param hflip: whether to flip the image horizontally
        '''
        if hflip or vflip:
            if hflip and vflip:
                c = -1
            else:
                c = 0 if vflip else 1
            image = cv2.flip(image, flipCode=c)
        return image 
    
    def save(self, save_path, image, vflip, hflip, angle, scale):
        output_filename = os.path.join(save_path, f"{self.name}_{vflip}_{hflip}_{angle:003}_{scale:.4f}.{target_filetype}")
        cv2.imwrite(output_filename, image)
        return output_filename

    def image_augment(self, save_path): 
        '''
        Create the new image with imge augmentation
        :param path: the path to store the new image
        ''' 
        img = self.image.copy()

        vflip, hflip = random.random()<=vflip_probability, random.random()<=hflip_probability
        rand_angle = random.randint(*random_angle_range)
        rand_scale = random.uniform(*zoom_range)
        
        img = self.flip(img, vflip=vflip, hflip=hflip)
        img = self.rotate(img, angle=rand_angle, scale=rand_scale)

        output_filename = self.save(save_path, img, vflip, hflip, rand_angle, rand_scale)
        print(output_filename)
        return output_filename
    
    
if __name__ == "__main__":
    files = glob.glob(f"{os.getcwd()}/*.{origin_filetype}", recursive=True)
    output_path = os.path.join(os.getcwd(), "output") 
    os.makedirs(output_path, exist_ok=True)

    for file in files:
        raw_image = Data_augmentation(file)
        raw_image.image_augment(output_path)
