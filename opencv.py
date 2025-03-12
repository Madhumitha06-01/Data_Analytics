import cv2 
import os
import numpy as np
img_path = os.path.join('.','ls','f2.jpg')
img = cv2.imread(img_path)
cv2.imshow("Image",img)

# Print the image shape 
print(img.shape)
# {or} Print the image shape 
img_height, img_width, channels = img.shape
print(f"Image Shape: {img.shape}")
print(f"Height: {img_height}, Width: {img_width}, Channels: {channels}")
cv2.waitKey(0)
cv2.destroyAllWindows()

# resize the img
img_resize = cv2.resize(img,(400,450))
cv2.imshow("frame",img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

# grey color
grey_color = cv2.cvtColor(img_resize,cv2.COLOR_BGR2GRAY)
cv2.imshow("grey_img",grey_color)
img_rgb = cv2.cvtColor(img_resize,cv2.COLOR_BGR2RGB)
cv2.imshow("rgb_img",img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

# crop the image
crop_img = img[0:410,0:510]
cv2.imshow('img',crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Types of Blur image
kernel_size = 7 # kernel size to be odd number
img_blur = cv2.blur(img,(kernel_size,kernel_size))
cv2.imshow("image_blur",img_blur)
img_guassion = cv2.GaussianBlur(img,(kernel_size,kernel_size),5)
cv2.imshow("img_guassion",img_guassion)
img_median = cv2.medianBlur(img,kernel_size)
cv2.imshow("img_median",img_median)
img_canny = cv2.Canny(img,100,200)
cv2.imshow("canny",img_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Write a text on image
#(img, text, position, font, font_scale, color, thickness, line_type)
text_img = cv2.putText(img,"Homey",(600,100),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(255, 0, 0),2,cv2.LINE_AA)
cv2.imshow("text_img",text_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# horizontall & verticall stack
h_img = np.hstack((img_resize,img_resize))
cv2.imshow("h_img",h_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
v_img = np.vstack((img_resize,img_resize))
cv2.imshow("v_img",v_img)

# use thresh 
img2_path = os.path.join('.','ls','0bc338ec-test_173_jpg.rf.e2c0de258fec36a15cea6d01c425f738.jpg')
img2 = cv2.imread(img2_path)
cv2.imshow("Image",img2)

img2_grey = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img2_grey,127,255,cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours: # count the pixel it means the img color and brightness area counter
    print(cv2.contourArea(cnt))
    # draw bounding box 
    x1,y1,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img2,(x1,y1),(x1+w, y1+h),(0,255,0),2)

cv2.imshow("thresh",thresh)
cv2.imshow("img",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()