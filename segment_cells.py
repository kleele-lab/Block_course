import napari 
import os
 
import h5py as h
import numpy as np

dir = r"X:\Kleele\Nov_2024\02-Analysis\241108_RPE1_drug_treatments_screen\Ilastik_segmentation"
save_dir = r"X:\Kleele\Nov_2024\02-Analysis\241108_RPE1_drug_treatments_screen\cell_masks"

already_list = os.listdir(save_dir)

for file in os.listdir(dir):
    if file.endswith('_decon.h5'):
        basename = file.split('.')[0]
        # check that we did not already do this one
        if not basename + '_cell_mask.npy' in already_list:
            # take max projection to make the cell mask
            img = np.max(h.File(os.path.join(dir,file))['data'][:,:,:],axis=0)

            viewer = napari.view_image(img,name=basename,colormap='grey')
            layer2 = np.zeros(img.shape).astype(int)
            viewer.add_labels(layer2, name='cell')

            input('press enter to save ')

            cell_layer = viewer.layers['cell'].data
            np.save(os.path.join(save_dir,basename +'_cell_mask.npy'),cell_layer) 

            viewer.close()