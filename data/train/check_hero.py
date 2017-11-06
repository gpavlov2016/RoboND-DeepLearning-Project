#By tokyo_adam 4-10-17 
import cv2
import numpy as np
import glob, os

#set to the directory where your masks are saved
img_dir = "masks/"

total_files = 0
total_hero = 0
total_back = 0
total_other = 0

os.chdir(img_dir)
for file in glob.glob("*.png"):
	total_files +=1

	img = cv2.imread(file)
	blue = img[:,:,0]
	green = img[:,:,1]
	red = img[:,:,2]

	if np.any(blue == 255):
		total_hero += 1
	else:
		#print(file)
		img_file = file.replace('mask', 'cam1')
		img_file = img_file.replace('png', 'jpeg')
		img_file = '../images/' + img_file
		if not os.path.isfile(img_file):
			img_file = img_file.replace('_cam1', 'cam1')
		if not os.path.isfile(img_file):
			print('fail') 
		os.remove(file)
		os.remove(img_file)

	if np.any(green == 255):
		total_other += 1

	if np.any(red== 255):
		total_back += 1

percent_hero = 100. * total_hero / total_files
percent_other = 100. * total_other / total_files
percent_back = 100. * total_back / total_files

print (percent_hero, "percent of files contain the hero")
print (percent_other, "percent of files contain the other people")
print (percent_back, "percent of files contain the background")
