import cv2
import numpy as np
import glob

def change_image_sizes(in_dir,out_dir,size=(50,50)):
# make sure all sign paths are the format of *.jpg
    img_paths = glob.glob(in_dir+"/*.jpg")

    for img_path in img_paths:
        img = cv2.imread(img_path)
        img = cv2.resize(img, size)
        name = img_path.split('/')[1]
        cv2.imwrite(out_dir+'/'+name,img)

if __name__ == '__main__':
    in_dir = 'neg'
    out_dir = '__tmp__'
    size = (50,50)
    change_image_sizes(in_dir,out_dir,size=size)
    print('[INFO] Changed all images from ',in_dir,'to',out_dir, ' resized to ', size)
