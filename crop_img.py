import cv2
import matplotlib.pyplot as plt

path_img = 'E:/2 MASTER/Memoire/06-27-2021'

img_org = cv2.imread(path_img+'CHNCXR_0003_0')
img_mask = cv2.imread(path_img+'CHNCXR_0003_0_predict')
##Resizing images
img_org = cv2.resize(img_org, (400,400))
img_mask = cv2.resize(img_mask, (400,400))

for h in range(len(img_mask)):
    for w in range(len(img_mask)):
        if img_mask[h][w][0] == 0:
            for i in range(3):
                img_org[h][w][i] = 0
        else:
            continue
            
plt.imshow(img_org)