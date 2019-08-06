# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 08:50:29 2019

@author: -Ripples

数据增强，旋转
"""
import os
import sys
sys.path.append('..')
import torch
from PIL import Image
from torchvision import transforms as tfs
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder

'''
im = Image.open('dataset/1_0072.png')
im_new = tfs.RandomVerticalFlip()(im)
rot_im = tfs.RandomRotation(45)(im)

rot_im.save('./test.png')
'''
data_transform = transforms.Compose([
        #transforms.Resize(299),
        #transforms.CenterCrop(299),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5],
                    	     std=[0.5, 0.5, 0.5])
    ])
train_dataset = ImageFolder(root='artist_distribute',transform=data_transform)

num_epoch = 1
print(train_dataset.class_to_idx)
#print(train_dataset.imgs)

def fi(string,jj):
    ck = 0
    for j in range(len(string)-1,0,-1):
        if (string[j] == '\\'):
            ck = j
            break
    #print(' ',string)
    #print(ck)
    new_str = string[:ck+1] + 'a'+ str(jj) + string[ck+1:]
    return new_str
    
total = 0
print('starting...')
for i, data in enumerate(train_dataset.imgs):
    inputs, labels = data
    im = Image.open(inputs)
    
    for j in range(num_epoch):
        rot_im = tfs.RandomRotation(30)(im)
        new_str = fi(inputs,j)
        #print('j=',j)
        #print(new_str)
        rot_im.save(new_str)
        total += 1
    
    
    im_new = tfs.RandomHorizontalFlip(p=1)(im)
    new_str = fi(inputs, 'c')
    #print(new_str)
    im_new.save(new_str)
    total += 1
    os.remove(inputs)
        
    #im_new = tfs.RandomCrop(256, padding=4, pad_if_needed=False, fill=0, padding_mode='edge')(im)
    #rint(im_new)
    
print('total = ',total)
print('Success~')
        
    