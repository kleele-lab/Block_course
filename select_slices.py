# select slice and segment cell area 

import numpy as np
import pandas as pd
import h5py as h
import napari
import os

from pathlib import Path
from skimage.io import imread

date = '240705'

#load images
folder = r"Y:\Koen\02 - Data\2024\07\240705_RPE1_palbo_8d_pkmo_iSIM"
imgs = Path(folder).rglob('*decon.ome.tif')

base_dir = r"Y:\Koen\01 - Analyses\RPE1_mito_lengths"
save_dir = os.path.join(base_dir,date,'img_slices')
cell_dir = os.path.join(base_dir,date, 'cell_segmentation')

if not os.path.exists(os.path.join(base_dir, date)):
    os.mkdir(os.path.join(base_dir, date))

if not os.path.exists(save_dir):
    os.mkdir(save_dir)

if not os.path.exists(cell_dir):
    os.mkdir(cell_dir)

already_list = [filename.split('_slice')[0] for filename in os.listdir(save_dir)]

for file in imgs:
    basename = os.path.basename(file)
    img_name = basename.split('.')[0]
    if img_name not in already_list:
        img = imread(file)
        print(img.shape)
        if img.shape[0] < 22:


            viewer = napari.view_image(img[:,:,:],name=img_name)

            slice = input('enter good z-slice')

            img_slice = img[int(slice),:,:]

            hf = h.File(os.path.join(save_dir,img_name + f'_slice_{slice}.h5'), 'w')
            hf.create_dataset('data',data=img_slice)
            hf.close()

            viewer.close()

            viewer = napari.view_image(img_slice, name=img_name)
            layer = np.zeros(img_slice.shape).astype(int)
            viewer.add_labels(layer, name='Cell')

            
            input('press enter to save, make backgrounds for each cell with the same number ')

            cells = viewer.layers['Cell'].data
            np.save(os.path.join(cell_dir,img_name +'_cell_mask.npy'),cells)

            viewer.close()
