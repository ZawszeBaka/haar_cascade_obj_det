import urllib.request
import cv2
import numpy as np
import os

def store_raw_images(num=1000):
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n09436708'
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1

    if not os.path.exists('neg'):
        os.makedirs('neg')

    neg_image_urls = neg_image_urls.split('\n')
    print('[INFO] max image urls : ', len(neg_image_urls))
    for i in neg_image_urls:
        try:
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img,size)
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1

            if pic_num % 100 == 0 :
                print('[INFO] Gathered ', pic_num , '/', num)

            if pic_num == num:
                break

        except Exception as e:
            print(str(e))

    print('[INFO] Gathering Done ! Total ', pic_num , ' pics ')

if __name__ == '__main__':
    store_raw_images(num=1000)
