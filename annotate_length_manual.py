import napari 
import os
 
import h5py as h
import numpy as np

img_dir = r""
save_dir = r""

already_list = os.listdir(save_dir)

for file in os.listdir(dir):
    if file.endswith('_decon.tif'):
        basename = file.split('.')[0]
        # check that we did not already do this one
        if not basename + '_mito_lengths.csv' in already_list:
            # take max projection to make the cell mask
            img = np.max(h.File(os.path.join(dir,file))['data'][:,:,:],axis=0)

            viewer = napari.view_image(img,name=basename,colormap='grey')
            layer2 = np.zeros(img.shape).astype(int)
            viewer.add_labels(layer2, name='cell')

            input('press enter to save ')

            cell_layer = viewer.layers['cell'].data
            np.save(os.path.join(save_dir,basename +'_cell_mask.npy'),cell_layer) 

            viewer.close()