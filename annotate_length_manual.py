import napari 
import os
import csv

import h5py as h
import numpy as np
import pandas as pd



dir = r"Z:\Kleele\Nov_2024\02-Analysis\241108_RPE1_drug_treatments_screen\Ilastik_segmentation"
save_dir = r"Z:\Kleele\Nov_2024\02-Analysis\241108_RPE1_drug_treatments_screen\manual_lengths"

already_list = os.listdir(save_dir)

for file in os.listdir(dir):
    if file.endswith('_decon_mito.h5'):
        basename = file.split('.')[0]
        # check that we did not already do this one
        if not basename + '_mito_lengths.csv' in already_list:
            # get image
            img = h.File(os.path.join(dir,file))['data'][:,:,:]

            viewer = napari.view_image(img,name=basename,colormap='grey')
            viewer.add_shapes(name='mito_lengths', ndim=2)

            input('press enter to save ')

            lengths = viewer.layers['mito_lengths'].data
            
            # save as rows to a csv
            file = open(os.path.join(save_dir,basename + '_mito_lengths.csv'), 'w')
            a = csv.writer(file)
            a.writerows(lengths)
            file.close()

            viewer.close()