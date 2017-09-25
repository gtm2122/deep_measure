# This script is to average the annotations given by deep matching

import matplotlib.pyplot as plt
import scipy.misc
import numpy as np
import os
import shutil
path_to_file = '/data/gabriel/deep_measure/matched_im/'
path_to_orig = '/data/gabriel/deep_measure/dataset/'
def get_u(s):
	return [i for i,j in enumerate(s) if (j=='_')][0]+1

for i in os.listdir(path_to_file):
	img = plt.imread(path_to_file+i)
	yellow_idx = np.where(np.logical_and(np.logical_and(img[100:,:,0]==1,img[100:,:,1]==1),img[100:,:,2]==0))
	blue_idx = np.where(np.logical_and(np.logical_and(img[100:,:,2]==1,img[100:,:,1]==1),img[100:,:,0]==0))
	
	#break

	print(i)

	yellow_avg_row = 100+int(yellow_idx[0].mean())
	blue_avg_row = 100+int(blue_idx[0].mean())

	print(yellow_avg_row)
	print(blue_avg_row)

	yellow_top_idx = np.where(np.logical_and(np.logical_and(img[:yellow_avg_row,:,0]==1,
		img[:yellow_avg_row,:,1]==1),img[:yellow_avg_row,:,2]==0))


	blue_top_idx = np.where(np.logical_and(np.logical_and(img[:blue_avg_row,:,0]==0,
		img[:blue_avg_row,:,1]==1),img[:blue_avg_row,:,2]==1))

	yellow_avg_top_idx = np.array([yellow_top_idx[0].mean(),yellow_top_idx[1].mean()]).astype(int)

	blue_avg_top_idx = np.array([blue_top_idx[0].mean(),blue_top_idx[1].mean()]).astype(int) 

	yellow_bot_idx = np.where(np.logical_and(np.logical_and(img[yellow_avg_row:,:,0]==1,
		img[yellow_avg_row:,:,1]==1),img[yellow_avg_row:,:,2]==0))


	blue_bot_idx = np.where(np.logical_and(np.logical_and(img[blue_avg_row:,:,0]==0,
		img[blue_avg_row:,:,1]==1),img[blue_avg_row:,:,2]==1))

	yellow_avg_bot_idx = np.array([yellow_avg_row+yellow_bot_idx[0].mean(),yellow_bot_idx[1].mean()]).astype(int)

	blue_avg_bot_idx = np.array([blue_avg_row+blue_bot_idx[0].mean(),blue_bot_idx[1].mean()]).astype(int)

	print(yellow_avg_bot_idx)
	print(yellow_avg_top_idx)

	print(blue_avg_bot_idx)
	print(blue_avg_top_idx)

	img_orig = plt.imread(path_to_orig+i[get_u(i):i.find('jpg')+3])

	img_orig[yellow_avg_bot_idx[0]-2:yellow_avg_bot_idx[0]+2,yellow_avg_bot_idx[1]-2:yellow_avg_bot_idx[1]+2,0]=255
	img_orig[yellow_avg_bot_idx[0]-2:yellow_avg_bot_idx[0]+2,yellow_avg_bot_idx[1]-2:yellow_avg_bot_idx[1]+2,1]=255
	img_orig[yellow_avg_bot_idx[0]-2:yellow_avg_bot_idx[0]+2,yellow_avg_bot_idx[1]-2:yellow_avg_bot_idx[1]+2,2]=0

	img_orig[yellow_avg_top_idx[0]-2:yellow_avg_top_idx[0]+2,yellow_avg_top_idx[1]-2:yellow_avg_top_idx[1]+2,0]=255
	img_orig[yellow_avg_top_idx[0]-2:yellow_avg_top_idx[0]+2,yellow_avg_top_idx[1]-2:yellow_avg_top_idx[1]+2,1]=255
	img_orig[yellow_avg_top_idx[0]-2:yellow_avg_top_idx[0]+2,yellow_avg_top_idx[1]-2:yellow_avg_top_idx[1]+2,2]=0

	img_orig[blue_avg_bot_idx[0]-2:blue_avg_bot_idx[0]+2,blue_avg_bot_idx[1]-2:blue_avg_bot_idx[1]+2,0]=0
	img_orig[blue_avg_bot_idx[0]-2:blue_avg_bot_idx[0]+2,blue_avg_bot_idx[1]-2:blue_avg_bot_idx[1]+2,1]=255
	img_orig[blue_avg_bot_idx[0]-2:blue_avg_bot_idx[0]+2,blue_avg_bot_idx[1]-2:blue_avg_bot_idx[1]+2,2]=255

	img_orig[blue_avg_top_idx[0]-2:blue_avg_top_idx[0]+2,blue_avg_top_idx[1]-2:blue_avg_top_idx[1]+2,0]=0
	img_orig[blue_avg_top_idx[0]-2:blue_avg_top_idx[0]+2,blue_avg_top_idx[1]-2:blue_avg_top_idx[1]+2,1]=255
	img_orig[blue_avg_top_idx[0]-2:blue_avg_top_idx[0]+2,blue_avg_top_idx[1]-2:blue_avg_top_idx[1]+2,2]=255

	# plt.imshow(img_orig)
	# plt.show()
	
	scipy.misc.imsave('/data/gabriel/deep_measure/for_pruning/'+i[get_u(i):i.find('jpg')+3]+'.png',img_orig)

	break

	