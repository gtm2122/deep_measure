import pandas as pd
import os
from shutil import copyfile

# d = pd.ExcelFile('/data/Gurpreet/Echo/Excel_Files/VC16_04082017_ArrangeData.xlsx').parse('All_Data')

# name = []

# names = d['Pat Name']
# Vids = d['Vid Name']

# ge_vings = [i for i,ele in enumerate(list(d['Manufacturer'])) if ele=='GE Vingmed Ultrasound']

# pla = [i for i,ele in enumerate(list(d['Main_Class'])) if ele=='PLA']

# #print(len(pla))

# pla_ge = list(set(pla).intersection(set(ge_vings)))

# img_names = [str(names[i])+'_'+str(Vids[i])+'_' for i in pla_ge]


# print(img_names)
# import pickle

# pickle.dump(img_names,open('list_of_images.pkl','rb'))
import pickle

import matplotlib.pyplot as plt

img_names = pickle.load(open('list_of_images.pkl','rb'))

import scipy.misc
import shutil
def find_s(s):
	return [i for i,j in enumerate(s) if j=='_'][1]


for i in os.listdir('/data/Gurpreet/RUNS/VC_16/SET1/dataset/train/PLA/'):
	
	if(i[:find_s(i)+1] in img_names):

		shutil.copyfile('/data/Gurpreet/RUNS/VC_16/SET1/dataset/train/PLA/'+i,'/data/gabriel/deep_measure/dataset/'+i)
for i in os.listdir('/data/Gurpreet/RUNS/VC_16/SET1/dataset/val/PLA/'):
	if(i[:find_s(i)+1] in img_names):

		shutil.copyfile('/data/Gurpreet/RUNS/VC_16/SET1/dataset/val/PLA/'+i,'/data/gabriel/deep_measure/dataset/'+i)

for i in os.listdir('/data/Gurpreet/RUNS/VC_16/SET1/dataset/test/PLA/'):
	if(i[:find_s(i)+1] in img_names):

		shutil.copyfile('/data/Gurpreet/RUNS/VC_16/SET1/dataset/test/PLA/'+i,'/data/gabriel/deep_measure/dataset/'+i)
