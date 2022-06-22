# -*- coding: utf-8 -*-
import tensorflow as tf
import sys
import matplotlib.image as mpimage
import matplotlib.pyplot as plt
import os
from os.path import join
from PIL import Image
sys.path.append('matching-with-gans')
import util
from google.colab import files


temp = files.upload()
temp = list(temp.keys())
temp = temp[0]
 
img1_path = os.path.join("/content/matching-with-gans/upload", temp)
img1_filename = os.path.basename(img1_path)
img1_wo_ext = img1_filename.split(".")[0]
print("upload img1 file here:", img1_path)
 
temp = files.upload()
temp = list(temp.keys())
temp = temp[0]
 
img2_path = os.path.join("/content/matching-with-gans/upload", temp)
img2_filename = os.path.basename(img2_path)
img2_wo_ext = img2_filename.split(".")[0]
print("upload img2 file here:", img2_path)

Raw_img_dir = '/content/matching-with-gans/upload'

Aligned_img_dir = '/content/matching-with-gans/outputs/aligned'
Plojected_img_dir = '/content/matching-with-gans/outputs/projected'
Manipulated_img_dir = '/content/matching-with-gans/outputs/manipulated'
Interpolated_img_dir = '/content/matching-with-gans/outputs/interpolated'


 
im_raw = mpimage.imread(join(Raw_img_dir, img1_filename))
im_aligned = mpimage.imread(join(Aligned_img_dir, img1_wo_ext+"_01.jfif"))
util.plot_row([im_raw, im_aligned], annot_list=['original', 'aligned'])
 
 
im_aligned = mpimage.imread(join(Aligned_img_dir, img1_wo_ext+"_01.jfif"))
im_projected = mpimage.imread(join(Aligned_img_dir, img1_wo_ext+"_01.jfif"))
util.plot_row([im_aligned, im_projected], annot_list=['aligned', 'projected'])
 
ATTRS_TO_ALTER = 'ACHG'

Image.open(join(Manipulated_img_dir, img1_wo_ext+"_01.jfif"))
 
Image.open(join(Interpolated_img_dir, img2_wo_ext + "_01_" + img1_wo_ext +"_01.png"))
