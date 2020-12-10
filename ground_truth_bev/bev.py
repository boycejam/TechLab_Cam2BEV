import cv2
import numpy as np
import matplotlib.pyplot as plt

imgs = './images-2-23-14-04-04'

SIZE = 1001
# a=["%07d" % x for x in range(SIZE)]
a = ["%07d" % x for x in range(1000, 1000 + SIZE * 500, 500)]

# roll and pitch and zheight

for i in range(0, SIZE):
   
    img_num = a[i]

    IMAGE_H = 480
    IMAGE_W = 640

    src = np.float32([[0, IMAGE_H], [IMAGE_W, IMAGE_H], [0, 0], [IMAGE_W, 0]])
    dst = np.float32([[290, IMAGE_H],[330, IMAGE_H],[0, 0],[IMAGE_W, 0]])
    M = cv2.getPerspectiveTransform(src, dst) # The transformation matrix
    Minv = cv2.getPerspectiveTransform(dst, src) # Inverse transformation

    # process image for training
    image = './train/t_0_0_' + img_num + '.png'
    img = cv2.imread(image) # Read the test img
    img = img[200:IMAGE_H, 0:IMAGE_W] # Apply np slicing for ROI crop
    warped_img = cv2.warpPerspective(img, M, (IMAGE_W, IMAGE_H)) # Image warping
    warped_img = cv2.rotate(warped_img, cv2.cv2.ROTATE_90_CLOCKWISE) 
    saved_img = './train/warp/t_0_0_' + img_num + '.png'
    cv2.imwrite(saved_img, warped_img)


    # process image for validation (new)
    image = './val/v_0_' + img_num + '.png'
    img = cv2.imread(image) # Read the val img
    img = img[200:IMAGE_H, 0:IMAGE_W] # Apply np slicing for ROI crop
    warped_img = cv2.warpPerspective(img, M, (IMAGE_W, IMAGE_H)) # Image warping
    warped_img = cv2.rotate(warped_img, cv2.cv2.ROTATE_90_CLOCKWISE) 
    saved_img = './val/warp/v_0_' + img_num + '.png'
    cv2.imwrite(saved_img, warped_img)

