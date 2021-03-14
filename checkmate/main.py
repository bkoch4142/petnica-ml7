import os
import PIL
from PIL import Image
import numpy as np

chessboard_dim=8
black_tile_px_val=[180, 136, 102, 255]
white_tile_px_val=[240, 217, 183, 255]

test_case=0

data_pth=os.path.join('checkmate\\data\\public\set\\',str(test_case))

img_pths={}
img_pths['input']=os.path.join(data_pth,str(test_case)+'.png')

for root, dirs, files in os.walk(data_pth, topdown=False):
    for name in files:
        if not name.split('.')[0].isnumeric():
            desc=os.path.normpath(root).split(os.path.sep)[-1]
            dict_key_name=desc+'_'+name.split('.')[0]
            img_pths[dict_key_name]=os.path.join(root,name)


a=np.asarray(Image.open(img_pths['input']))
print('end')
