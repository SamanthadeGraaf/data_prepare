# 03-11-2020 Samantha de Graaf
# Data preperation for train_model.py
# Sorts list of images and masks to:
#      image_x  
#           image
#               image_x.png
#           mask
#               image_x.png
#               etc.
# Change the path to images and destination in step 1. 

# 0. import packages
import os
import shutil
import pathlib
from tqdm import tqdm
from skimage.io import imread, imshow
from pathlib import Path

# 1. Read in data file
PATH_TO_IMAGE = 'C:/Users/Samantha/Documents/BIGR_Internship/CT_datasets/luu_png/image/'
PATH_TO_MASK = 'C:/Users/Samantha/Documents/BIGR_Internship/CT_datasets/luu_png/mask/'
DESTINATION = 'C:/Users/Samantha/Documents/BIGR_Internship/DATA/Luu_sorted_down/train/'

# 2. Get image ID's
path_ids = next(os.walk(PATH_TO_IMAGE))[2]
path_ids2 = next(os.walk(PATH_TO_MASK))[2]
print(path_ids)

# 3. Create main folder - subfolder 'image' and move images
for n, id_ in tqdm(enumerate(path_ids), total=len(path_ids)):
    path = PATH_TO_IMAGE + id_
    # MAIN FOLDER - create folder with the same name as image
    ids = Path(path).stem
    ids_path = os.path.join(DESTINATION, ids) 
    os.mkdir(ids_path) 
    print("Directory '%s' created" %ids) 
    
    # IMAGE - create subfolder named image
    subdir_im = 'image'
    subdir_path = os.path.join(ids_path, subdir_im)
    os.mkdir(subdir_path) 
    print("Directory '%s' created" %subdir_im) 

    # IMAGE - Move images in this subfolder
    shutil.move(path, subdir_path + '/'+ ids + '.png')

# 4. Create subfolder 'mask' and move images
for n, id_ in tqdm(enumerate(path_ids2), total=len(path_ids2)):
    path = PATH_TO_MASK + id_
    ids = Path(path).stem
    ids_path = os.path.join(DESTINATION, ids) 
        
    # MASK - create subfolder named mask
    subdir_mask = 'mask'
    subdir_path = os.path.join(ids_path, subdir_mask)
    os.mkdir(subdir_path) 
    print("Directory '%s' created" %subdir_mask) 

    # MASK - Move images in this subfolder
    shutil.move(path, subdir_path + '/'+ ids + '.png')
print('Sorting training data done!')

# 5. Downsample training images to 256x256
IMG_HEIGHT = 256
IMG_WIDTH 256
print('Start downsampling images')
for n, id_ in tqdm(enumerate(train_ids), total=len(train_ids)):
    path = DESTINATION + id_
    img = Image.open(path +  '/image/' + id_ + '.png')
    img = img.resize((IMG_WIDTH,IMG_HEIGHT),Image.ANTIALIAS) 
    img.save(path+ '/image/' + id_ + '.png')
    
    mask = Image.open(path +'/mask/' + id_ + '.png')
    mask = mask.resize((IMG_WIDTH,IMG_HEIGHT),Image.ANTIALIAS)
    mask.save(path+'/mask/' + id_ + '.png')
   
    
