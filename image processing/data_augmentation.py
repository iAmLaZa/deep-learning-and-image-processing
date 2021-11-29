
import numpy as np
import cv2
import os






def flip_in(rgb_path,  gt_path,entries):
    total = len(entries)
    actuel = 1
    for entry in entries:
        
        rgb = cv2.imread(rgb_path + "/" + entry[0], cv2.IMREAD_UNCHANGED)
        
        gt = cv2.imread(gt_path + "/" + entry[1], cv2.IMREAD_UNCHANGED)

        #flip 1 miroir
        img_flip_1=cv2.flip(rgb,1)
        cv2.imwrite(rgb_path + "/" + entry[0][0:-4]+ "_flip_1"+entry[0][-4:], img_flip_1)

        gt_flip_1=cv2.flip(gt,1)
        cv2.imwrite(gt_path + "/" + entry[1][0:-4]+ "_flip_1"+entry[1][-4:], gt_flip_1)
       


def flip_dg(rgb_path,  gt_path,entries):
    
    total = len(entries)
    actuel = 1

    for entry in entries:
        
        rgb = cv2.imread(rgb_path + "/" + entry[0], cv2.IMREAD_UNCHANGED)
        
        gt = cv2.imread(gt_path + "/" + entry[1], cv2.IMREAD_UNCHANGED)
        # rotation 90 degres rgb depth gt (clockwise)
        img_rotate_90 = cv2.rotate(rgb, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(rgb_path + "/" + entry[0][0:-4]+ "_flip90"+entry[0][-4:], img_rotate_90)

        

        gt_rotate_90 = cv2.rotate(gt, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(gt_path + "/" + entry[1][0:-4]+ "_flip90"+entry[1][-4:], gt_rotate_90)

        # rotation 270 degres rgb depth gt (clockwise)
        img_rotate_270 = cv2.rotate(rgb, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite(rgb_path + "/" + entry[0][0:-4]+ "_flip270"+entry[0][-4:], img_rotate_270)

       

        gt_rotate_270 = cv2.rotate(gt, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite(gt_path + "/"  + entry[1][0:-4]+ "_flip270"+entry[1][-4:], gt_rotate_270)

        # rotation 180 degres rgb depth gt (clockwise)
        img_rotate_180 = cv2.rotate(rgb, cv2.ROTATE_180)
        cv2.imwrite(rgb_path + '/'+entry[0][0:-4]+ "_flip180"+entry[0][-4:] , img_rotate_180)

        gt_rotate_180 = cv2.rotate(gt, cv2.ROTATE_180)
        cv2.imwrite(gt_path  + '/'+entry[1][0:-4]+ "_flip180"+entry[1][-4:], gt_rotate_180)

        



rgb_path='path_img'
gt_path='path_gt'

rgb_images = os.listdir(rgb_path)
    
gt_images = os.listdir(gt_path)

entries = list(zip(rgb_images, gt_images))
flip_dg(rgb_path,gt_path ,entries )


rgb_images = os.listdir(rgb_path)
    
gt_images = os.listdir(gt_path)
entries = list(zip(rgb_images, gt_images))
flip_in(rgb_path,gt_path ,entries )

