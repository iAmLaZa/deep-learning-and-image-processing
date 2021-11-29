import shutil
import os
import regex as re



src_gt='path_gt'
dest='path_dest_gt'

src_img='path_umg'
dest2='path_dest_img'


files_gt=os.listdir(src_gt)
files_img=os.listdir(src_img)

i=0
cpt=0
limit=(len(files_img)*0.2)
while(cpt<limit):
    
    sub=files_img[i]
    sub=sub[0:-4]
    if((sub+".png") in files_gt):
      shutil.move(src_img+'/'+files_img[i],dest2)
      shutil.move(src_gt+'/'+sub+".png",dest)
      i+=1
      cpt+=1
    else:
        if((sub+".tif") in files_gt):
          shutil.move(src_img+'/'+files_img[i],dest2)
          shutil.move(src_gt+'/'+sub+".tif",dest)
          
          i+=1
          cpt+=1
        else:
          i+=1




