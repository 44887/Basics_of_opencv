
#convert an image into grayscale

# Step 1:- Import the required packages
import cv2
# Step 2:- Load the images
img1=cv2.imread("hourse.jpg",1)
# Step 3:-  Convert the color into GRAYSCALE
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# Step 4:- Show the converted image to the user
cv2.imshow("Converted Image",gray)
# Step 5:- Save the image to the drive
cv2.imwrite("grayedimage.jpg",gray)

#convert an image into HSV

# Step 1:- Import the required packages
import cv2
# Step 2:- Load the images
img1=cv2.imread("image1.jpg",1)
# Step 3:-  Convert the color into HSV
hsv=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
# Step 4:- Show the converted image to the user
cv2.imshow("Converted Image",hsv)
# Step 5:- Save the image to the drive
cv2.imwrite("HSVimage.jpg",hsv)


#convert an image into RGB

# Step 1:- Import the required packages
import cv2
# Step 2:- Load the images
img1=cv2.imread("image1.jpg",1)
# Step 3:-  Convert the color into HSV
rgb=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
# Step 4:- Show the converted image to the user
cv2.imshow("Converted Image",rgb)
# Step 5:- Save the image to the drive
cv2.imwrite("RGBimage.jpg",rgb)

#List down all functions of opencv

# Step 1:- Import the required module
import cv2
# Now list down all the functions available in opencv
functions=dir(cv2)
for fun in functions:
    print(fun)
    print("\n")

