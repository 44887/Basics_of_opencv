#Access pixel of an image

#Step 1: Import the required packages
import numpy as np
import cv2
#Step 2: Load the image
img=cv2.imread("hourse_img.jpg",1)
'''You can access a pixel value by its row and column coordinates.
For BGR image, it returns an array of Blue, Green, Red values. 
For grayscale image, just corresponding intensity is returned.'''
#Step 3: Access the pixel values and store it in a variable
px=img[100,100]
# Step 4: Display the pixel values to the user
print("The pixel values of the coordinate [100,100] is ",px)

#access blue pixel of an image

#Step 1: Import the required packages
import numpy as np
import cv2
#Step 2: Load the image
img=cv2.imread("hourse_img.jpg",1)
'''You can access a pixel value by its row and column coordinates.
For BGR image, it returns an array of Blue, Green, Red values. 
For grayscale image, just corresponding intensity is returned.'''
#Step 3: Access the pixel values and store it in a variable
blue=img[100,100,0]# The pixels can be accesses using zero(0) based index
# Step 4: Display the pixel values to the user
print("The blue pixel values of the coordinate [100,100] is ",blue)


#access green pixel of an image

#Step 1: Import the required packages
import numpy as np
import cv2
#Step 2: Load the image
img=cv2.imread("hourse_img.jpg",1)
'''You can access a pixel value by its row and column coordinates.
For BGR image, it returns an array of Blue, Green, Red values. 
For grayscale image, just corresponding intensity is returned.'''
#Step 3: Access the pixel values and store it in a variable
green=img[100,100,1]# The pixels can be accesses using zero(0) based index
# Step 4: Display the pixel values to the user
print("The green pixel values of the coordinate [100,100] is ",green)


#access red pixel of an image

#Step 1: Import the required packages
import numpy as np
import cv2
#Step 2: Load the image
img=cv2.imread("hourse_img.jpg",1)
'''You can access a pixel value by its row and column coordinates.
For BGR image, it returns an array of Blue, Green, Red values. 
For grayscale image, just corresponding intensity is returned.'''
#Step 3: Access the pixel values and store it in a variable
red=img[100,100,2]# The pixels can be accesses using zero(0) based index
# Step 4: Display the pixel values to the user
print("The red pixel values of the coordinate [100,100] is ",red)


#modify pixel values of a particular coordinate

#Step 1: Import the required packages
import numpy as np
import cv2
#Step 2: Load the image
img=cv2.imread("hourse_img.jpg",1)
'''You can access a pixel value by its row and column coordinates.
For BGR image, it returns an array of Blue, Green, Red values. 
For grayscale image, just corresponding intensity is returned.'''
#Step 3: Access the pixel values and store it in a variable
px=img[100,100]
# Step 4: Display the pixel values to the user
print("The  pixel values of the coordinate [100,100] is ",px)
#Step 5: Modify the pixel values
img[100,100]=[230,100,264]
#Step 6: Print the modified pixel values
cv2.imshow("converted image",img)
print(" \nThe modified pixel value at coordinate [100,100] is  ",img[100,100])

#modify blue pixel value of an image

#Step 1: Import the required packages
import numpy as np
import cv2
#Step 2: Load the image
img=cv2.imread("hourse_img.jpg",1)
'''You can access a pixel value by its row and column coordinates.
For BGR image, it returns an array of Blue, Green, Red values. 
For grayscale image, just corresponding intensity is returned.'''
#Step 3: Access the pixel values and store it in a variable
blue=img.item(100,100,0)
# Step 4: Display the pixel values to the user
print("The blue pixel values of the coordinate [100,100] is ",blue)
#Step 5: Modify the pixel values
img.itemset((100,100,0),245)
#Step 6: Print the modified pixel values
print(" \nThe modified pixel value at coordinate [100,100] is  ",img[100,100,0])


#modify green pixel value of an image

#Step 1: Import the required packages
import numpy as np
import cv2
#Step 2: Load the image
img=cv2.imread("hourse_img.jpg",1)
'''You can access a pixel value by its row and column coordinates.
For BGR image, it returns an array of Blue, Green, Red values. 
For grayscale image, just corresponding intensity is returned.'''
#Step 3: Access the pixel values and store it in a variable
green=img.item(100,100,0)
# Step 4: Display the pixel values to the user
print("The green pixel values of the coordinate [100,100] is ",green)
#Step 5: Modify the pixel values
img.itemset((100,100,0),230)
#Step 6: Print the modified pixel values
print(" \nThe modified pixel value at coordinate [100,100] is  ",img[100,100,0])

#modify red pixel value of an image

#Step 1: Import the required packages
import numpy as np
import cv2
#Step 2: Load the image
img=cv2.imread("hourse_img.jpg",1)
'''You can access a pixel value by its row and column coordinates.
For BGR image, it returns an array of Blue, Green, Red values. 
For grayscale image, just corresponding intensity is returned.'''
#Step 3: Access the pixel values and store it in a variable
red=img.item(100,100,0)
# Step 4: Display the pixel values to the user
print("The red pixel values of the coordinate [100,100] is ",red)
#Step 5: Modify the pixel values
img.itemset((100,100,0),75)
#Step 6: Print the modified pixel values
print(" \nThe modified pixel value at coordinate [100,100] is  ",img[100,100,0])


#accesing shape of an image

# Step 1: Import the reuired packages
import cv2
import numpy as np
# Step 2: Load the image
img=cv2.imread("hourse_img.jpg",1)
# Access the shape of an image and store it in a variable
row,column,channel=img.shape
dimension=img.shape
# Print the image dimension
print("The dimension of an image is ",dimension)
print("The no of rows in an image is ", row)
print("The no of columns in an image is ",column)
print("The channels in an image is ",channel)


#accessing shape of a grayscale image

# Step 1: Import the reuired packages
import cv2
import numpy as np
# Step 2: Load the image
img=cv2.imread("hourse_img.jpg",0)
# Access the shape of an image and store it in a variable
rows,columns=img.shape
dimension=img.shape
# Print the image dimension
print("The dimension of an image is ",dimension)
print("The no of rows in an image is ", rows)
print("The no of columns in an image is ",columns)

#Step 1:- Import the required packages
import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,0,0]
#Step 2:- Load the image
img1 = cv2.imread('flower1.png')
# Step 3:- Make the border of different types by mentioning the arguments in it.
replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
# Step 4:- Plot all the borders
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()