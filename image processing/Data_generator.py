import tensorflow as tf
import os
import cv2
import numpy as np

img_w=512
img_h=512
img_ch=3

class Data_generator(tf.keras.utils.Sequence):
    def __init__(self,rgb_path,gt_path,batch_size):
        self.batch_size=batch_size
        self.length=len(os.listdir(rgb_path))


        self.rgb_path=rgb_path
        self.gt_path=gt_path

        self.indexes=np.arange(self.length)
        
        self.on_epoch_end()
        
    def on_epoch_end(self):
        np.random.shuffle(self.indexes)
        
        
    def __len__(self):
        return int(np.floor(self.length/self.batch_size))
        
    def __getitem__(self, index):
        indexes=self.indexes[index * self.batch_size:(index+1) *self.batch_size]
        x=np.empty((self.batch_size,512,512,3))

        y=np.empty((self.batch_size,512,512))

        cpt=0
        liste_rgb=os.listdir(self.rgb_path)
        liste_gt=os.listdir(self.gt_path)

        
        for i in indexes:
            
           
            
            rgb_input=cv2.imread(self.rgb_path+'/'+liste_rgb[i])
            rgb_input=cv2.cvtColor(rgb_input,cv2.COLOR_BGR2RGB)
            rgb_input=cv2.resize(rgb_input,(512,512))/255
                
                
            gt_input=cv2.imread(self.gt_path+'/'+liste_rgb[i][:-4]+".tiff",0)
            gt_input=cv2.resize(gt_input,(512,512))/255
                
            x[cpt, ]=rgb_input
            y[cpt, ]=gt_input
            cpt+=1
            
        return x,y