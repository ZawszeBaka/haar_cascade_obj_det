import positive_image_generator
from positive_image_generator import *

def creating_pos_image(_max = 2000):
	# make sure all sign paths are the format of *.jpg
	sign_paths = glob.glob("traffic_sign/*.jpg")
	signs = [ cv2.imread(sign_path)  for sign_path in sign_paths]

	# make sure all background paths are the format of *.jpg
	bg_paths = glob.glob("neg/*.jpg")
	bgs = [ cv2.imread(bg_path) for bg_path in bg_paths]

	num_signs_per_img = 1
	time = 1
	total_pos_imgs = len(sign_paths) * len(bg_paths) * num_signs_per_img * time

	info_lst = []

	print(' [INFO] Num signs ', len(sign_paths))
	print(' [INFO] Num background ', len(bg_paths))
	print(' [INFO] Num signs per img ', num_signs_per_img)
	print(' [INFO] Each bg is used ', time, 'time for each sign')
	print(' [INFO] Estimating...  about ',total_pos_imgs , 'positive images will be created !!')
	print('\n [INFO] Processing')

	i = 0

	for bg in bgs:
		for sign in signs:
			for num_signs in range(num_signs_per_img):
				for _ in range(time):
					random_size = np.random.randint(20)+10 # 10 -> 30
					pos, pt, w, h = processing(sign, bg, is_test = False, img_size=(50,50), sign_size = (random_size,random_size))
					file_name = str(i) + '.jpg'
					i += 1
					if i % 100 == 0 :
						print(' [INFO] ', i , '/', _max )

					# test = cv2.rectangle(pos, (pt[0],pt[1]), (pt[0]+w,pt[1]+h),(0,255,0),2)
					# cv2.imshow('test',test)
					# cv2.waitKey()
					# return

					info_lst.append(file_name + ' ' + str(num_signs+1) + ' ' + str(pt[0]) + ' ' + str(pt[1]) + ' ' + str(w) + ' ' + str(h))
					cv2.imwrite('info/'+file_name, pos)

					# created enough
					if i == _max:
						break
				if i == _max :
					break
			if i == _max :
				break
		if i == _max:
			break

	with open('info.lst', 'w') as f:
		f.write('\n'.join(info_lst))

if __name__ == '__main__':
	creating_pos_image(_max = 1600)
	print(' [INFO] done ! ')
