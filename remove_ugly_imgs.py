import os
import cv2
import numpy as np

def removing_uglies():
    match = False
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))

if __name__ == '__main__':
    ''' Place ugly images in directory 'uglies' '''

    removing_uglies()
    
    print('[INFO] Removed ugly images Done!')
    print('[INFO] After removing uglies, num of remained pics : ', len(os.listdir('neg')))
