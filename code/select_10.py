import os
import matplotlib.pyplot as plt 


def find_k(s,k,w):
	return [i for i,j in enumerate(s) if j==w][k-1]


import glob
dic= {}

for i in sorted(glob.glob('/data/gabriel/deep_measure/dataset/*.jpg')):

	if(i[find_k(i,5,'/')+1:find_k(i,3,'_')] not in dic):
		dic[i[find_k(i,5,'/')+1:find_k(i,3,'_')]] = []
	dic[i[find_k(i,5,'/')+1:find_k(i,3,'_')]].append(i[find_k(i,5,'/')+1:])

import random

img_name = []
#print(dic)
for i in dic:
	l = dic[i]
	#print(l[:10])
	random.shuffle(l)
	#print(l[:10])
	#break
	img_name+=l[:10]

#print(img_name[:25])
import shutil
for i in img_name:
	shutil.copyfile('/data/gabriel/deep_measure/dataset/'+i,'/data/gabriel/deep_measure/rand_10/'+i)

