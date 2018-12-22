import cv2
import numpy as np

import matplotlib.pyplot as plt

import glob

def roi_sign(sign):
	'''
		The image must be thresholded
	'''

	w = sign.shape[1]
	h = sign.shape[0]

	upper_boundary = dict()
	lower_boundary = dict()

	for x in range(w):
		# go down
		for y in range(h):
			if sign[y,x] <=0:
				upper_boundary[x] = y
				break
		else:
			print(" [WARNING] not found line!! ")

		# # go up
		rv = list(range(h))
		rv.reverse()
		for y in rv:
			if sign[y,x] <= 0:
				lower_boundary[x] = y
				break
		else:
			print(" [WARNING] not found line!! ")

	rs = np.copy(sign)

	for x in range(w):
		for y in range(h):
			try:
				if y <= lower_boundary[x] and y >= upper_boundary[x]:
					rs[y,x] = 255
				else:
					rs[y,x] = 0
			except:
				print(' [WARNING] KeyError ')

	return rs

def add_pts(img, pts):
	for i in range(pts.shape[0]):
		x = int(pts[i,0])
		y = int(pts[i,1])
		img = cv2.rectangle(img,(x-2,y-2),(x+2,y+2),(0,255,0),10)
	return img

def random_pts2():
    x2 = np.random.randint(100)
    y2 = np.random.randint(100) + 150
    x1 = np.random.randint(100) + 150
    y1 = np.random.randint(100)

    return np.float32([[50,50],[x1,y1],[x2,y2]])

def warp(img, pts2):

    pts1 = np.float32([[50,50],[200,50],[50,200]])

    M = cv2.getAffineTransform(pts1,pts2)

    dst = cv2.warpAffine(img,M,(img.shape[0]*2, img.shape[1]*2))

    return dst

def resize(gray, time):
	tmp = np.zeros((int(gray.shape[0]*time), int(gray.shape[1]*2)), dtype=np.uint8)
	tmp[tmp.shape[0]//2 - gray.shape[0]//2 : tmp.shape[0]//2 - gray.shape[0]//2 + gray.shape[0] ,
	 		      tmp.shape[1]//2 - gray.shape[1]//2 : tmp.shape[1]//2 - gray.shape[1]//2 + gray.shape[1]] = gray
	return tmp

def warped_roi_sign(warped_thresholded):
	y = np.nonzero(warped_thresholded)[0]
	x = np.nonzero(warped_thresholded)[1]

	return [min(x), min(y)] , max(x)-min(x)+1, max(y)-min(y)+1

def add_to_bg(bg, warped, thresholded_wapred_mask):
	first_pt, w, h = warped_roi_sign(thresholded_wapred_mask)

	rand_pos_x = np.random.randint(bg.shape[1]-w-1)
	rand_pos_y = np.random.randint(bg.shape[0]-h-1)

	for x in range(w):
		for y in range(h):
			if thresholded_wapred_mask[first_pt[1]+y,first_pt[0]+x] >= 200:
				bg[rand_pos_y+y,rand_pos_x+x] = warped[first_pt[1]+y,first_pt[0]+x]

	return bg , [first_pt[0]+rand_pos_x, first_pt[1]+rand_pos_y], w, h

def processing(sign, bg, is_test = False, img_size = (50,50), sign_size = (20,20)):
    ''' Main process here !  '''

    gray = cv2.cvtColor(sign, cv2.COLOR_BGR2GRAY)
    if len(bg.shape) == 3:
        bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)

    bg = cv2.resize(bg,img_size)
    pts2 = random_pts2()

    #
    resized_gray = resize(gray, 2)
    # ret, resized_gray = cv2.threshold(resized_gray, 100, 255, cv2.THRESH_BINARY)
    warped = warp(resized_gray,pts2)

    # mask
    ret, masked_gray = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    masked_gray = roi_sign(masked_gray)
    resized_mask = resize(masked_gray, 2)
    warped_mask = warp(resized_mask,pts2)

    # get region of sign after warping
    first_pt, w, h = warped_roi_sign(warped_mask)
    warped = warped[first_pt[1]:first_pt[1]+h , first_pt[0]:first_pt[0]+w]
    warped_mask = warped_mask[first_pt[1]:first_pt[1]+h , first_pt[0]:first_pt[0]+w]

    warped = cv2.resize(warped,sign_size)
    warped_mask = cv2.resize(warped_mask,sign_size)

    # add to bg
    pos, first_pt, w, h = add_to_bg(bg, warped, warped_mask)

    # add to bg
    if is_test:
        cv2.imshow('bg', bg)
        cv2.imshow('after adding to bg', pos)
        cv2.imshow('resized_gray', resized_gray)
        cv2.imshow('masked_gray', resized_mask)
        cv2.imshow('warped org', warped)
        cv2.imshow('warped_mask', warped_mask)
        cv2.waitKey()

    return pos, first_pt, w, h


if __name__ == '__main__':
    print(' [INFO] Don\'t run this file, run creating_pos_image.py instead  ')
