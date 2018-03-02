# Step 1:- import the packages
import cv2
#  Step 2:- Create an object to hold the image.
img=cv2.imread("hourse_img.jpg",0)#Here the first paramater could be any image file along with its format


#Read an image in color

import cv2
#  Step 2:- Create an object to hold the image.
        #Here the first paramater could be any image file along with its format.
        #Here  the cv2.IMREAD_COLOR flag will be use to read an image in the color
        #  which is in the BGR(Blue,Green, Red) which is the default
        #format of the imread() function.
img=cv2.imread("hourse_img.jpg",cv2.IMREAD_COLOR)
# The flag value cv.IMREAD_COLOR is used to read an image in the color. It is the default mode.

#Read an image in grayscale

# Step 1: - import the packages
import cv2
# Step 2:- Create an object to hold the image.
        #Here the first paramater could be any image file along with its format.
        #Here  the cv2.IMREAD_GRAYSCALE flag will be use to read an image in the color
         # which is in the BGR(Blue,Green, Red) which is the default
        #format of the imread() function.
img=cv2.imread("image1.jpg",cv2.IMREAD_GRAYSCALE)
# The flag value cv.IMREAD_GRAYSCALE is used to read an image in the GRARSCALE Format.


#This will read the image without performing any change in the color like in the case
#of color and grayscale ie. it reads the COLOR image in color format that ie BGR and GRAYSCALE image in grayscele format
# Step 1: -Import the required package
import cv2
# Step 2:- Create an image object or object to hold the image file in it.
img=cv2.imread("image1.jpg",cv2.IMREAD_UNCHANGED)


#Alternate ways to read an image in color,grayscale and unchanged format

#Step 1:- Import the required packages
import cv2
#Step 2:- Create an object to hold the image in it
    #Reading image in Color using Integer notation
img=cv2.imread("hourse_img.jpg",1)#The flag 1 is used to read the image in Color Mode.It is default mode
    #Reading image in Grayscale using Integer Notation
img1=cv2.imread("hourse_img.jpg",0)# The flag 0 is used to read the image in Grayscale Mode
    #Reading the image in unchanged mode.It reads the image without performing any color change operations on it.
img2=cv2.imread("hourse_img.jpg",-1)

#display an image

#import the packages
import cv2
# Create an object to hold the image.
img=cv2.imread("hourse_img.jpg",1)#Here the first paramater could be any image file along with its format.
cv2.imshow("UserImage",img)#The first paramter is any name or string which will be displayed as title and second is the image object
cv2.waitKey(0)#This is used to capture the keystroke from the user.As and when the user press any  of the key it will capture it.
cv2.destroyAllWindows()#This will destroy all the instances of the widnows which is created during


#display image in color

#Step 1:- Import the required packages
import cv2
#Step 2:- Create an object to read and hold the image in color format
img=cv2.imread("hourse_img.jpg",cv2.IMREAD_COLOR)
#Step 3:- Display the Image to the User
cv2.imshow("Displaying the image in color",img)
#Step 4:- Capture the keypress of the user
cv2.waitKey(0)
#Step 5:- Destory all the instances created
cv2.destroyAllWindows()

#read and disply image in grayscale

#Step 1:- Import the required Packages
import cv2
#Step 2:- Create an object to  read and store the image in grayscale
img1=cv2.imread("hourse_img.jpg",0)
#Step 3:- Display an image to the User
cv2.imshow("Displaying an image to the user in grayscale",img1)
#Step 4:- Capture anystroke from the user
cv2.waitKey(0)
#Step 5:- Destroy all the previously created instances
cv2.destroyAllWindows()

#read an image in unchanged format and disply it to user

#Step 1:- Import the required Packages
import cv2
#Step 2:- Create an object to  read and store the image in grayscale
img1=cv2.imread("hourse_img.jpg",-1)
#Step 3:- Display an image to the User
cv2.imshow("Displaying an image to the User unchanged",img1)
#Step 4:- Capture anystroke from the user
cv2.waitKey(0)
#Step 5:- Destroy all the previously created instances
cv2.destroyAllWindows()


#read an image and convert into another format after displaying it to the user

#Step 1:- Import the necessary packages
import cv2
# Step 2:- Create an object to hold the image
img=cv2.imread("hourse_img.jpg",cv2.IMREAD_COLOR)
# Step 3:- Display the Image to the User
cv2.imshow("Image",img)# Used to display the image to the user
'''The first argument will be the filename with format in which you want to save the file 
and second is the image object which holds the image file'''
#Step 4:- Convert and write an image in other format
cv2.imwrite("image1.png",img)#This will write an image in .png format having name as image1.
                             # The image is stored in current directory.
                             #User can also give the exact path where they want to store the image.
# Step 5:- Capture the key pressed by the User
cv2.waitKey(0)#This will wait for the user to press any key
#Step 6:- Destory all the previously Created Instances.
cv2.destroyAllWindows()# This will destroy all the windows Instances

#Distroy all previously created instances on press of specific key

# Step 1:- Import the necessary packages
import cv2
# Step 2:- Create an object to hold the image
img=cv2.imread("hourse_img.jpg",cv2.IMREAD_GRAYSCALE)
#Step 3:- Display an image to the User
cv2.imshow("Image",img)# Used to display the image
#Step  4:- Wait of the key pressed by the User
k=cv2.waitKey(0)#This will wait for the user to press 'a' key on the keyboard
#Step 5 Destory all the instances.
if k== ord('a'):               #it returns an integer
    cv2.destroyAllWindows()
    # This will destroy all the windows Instances when a key is pressed on the keyboard

#save an image and exit when 's' key is pressed and close when 'esc' is pressed

#Step 1 :- Import the required packages
import cv2
#Step 2:- Create an object to hold the image in it.
img = cv2.imread("hourse_img.jpg",0)
#Step 3:- Show an image to the User
cv2.imshow("Displaying Image to User",img)
#Step 4: Wait for the User to press the key on the keyboard
#If you are using 64-bit machine then you have to write the waitKey as mentioned over here otherwise
k = cv2.waitKey(0) & 0xFF
if k == 27: #Wait for the Esc Key to press
    cv2.destroyAllWindows()
elif k== ord('s'): # Wait for s key to save and exit
    cv2.imwrite("image23.png",img)
    cv2.destroyAllWindows()

#load an image in named window and make it resizable.

#WINDOW_NORMAL If this is set, the user can resize the window (no constraint).
#WINDOW_AUTOSIZE If this is set, the window size is automatically adjusted to fit the
    #  displayed image (see imshow() ), and you cannot change the window size manually.
#WINDOW_OPENGL If this is set, the window will be created with OpenGL support.

#Step 1 : Import the required packages
import cv2
# Step 2:- Create a named window which will hold the image
cv2.namedWindow("FIRSTIMAGE",cv2.WINDOW_NORMAL)
#Step 3:- Read an image and store it in the Object
img=cv2.imread("hourse_img.jpg",0)
#Step 4:- Display an image in the previously created named windows
cv2.imshow("FIRSTIMAGE",img)
#Step 5:- Wait for the key to be pressed by the user
cv2.waitKey(0)
#Step 5:- Destroy all the windows
cv2.destroyAllWindows()

#load an image in named window

#Step 1 : Import the required packages
import cv2
# Step 2:- Create a named window which will hold the image
cv2.namedWindow("Secondimage",cv2.WINDOW_AUTOSIZE)# it is the default mode.It automatically takes image size.
#Step 3:- Read an image and store it in the Object
img=cv2.imread("hourse_img.jpg",0)
#Step 4:- Display an image in the previously created named windows
cv2.imshow("Secondimage",img)
#Step 5:- Wait for the key to be pressed by the user
cv2.waitKey(0)
#Step 5:- Destroy all the windows
cv2.destroyAllWindows()

#convert an image from BGR to RGB format

#Step 1:- Import the required Packages
import cv2
# Step 2:- Create an object to hold the image
img=cv2.imread("hourse_img.jpg",1)
#Step 3:- Convert the Color Format
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#Step 4:- Show an image to the User and SAVE it
cv2.imshow("DISPLAYING IMAGE IN RGB FORMAT",rgb)
cv2.imwrite("BGR2RGB.jpg",rgb)
#Step 5:- Wait for the user to press any key
cv2.waitKey(0)
#Step 6:- Destroy all the windows Instances
cv2.destroyAllWindows()

#convert an image from BGR to HSV format

#Step 1:- Import the required Packages
import cv2
# Step 2:- Create an object to hold the image
img=cv2.imread("hourse_img.jpg",1)
#Step 3:- Convert the Color Format
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#Step 4:- Show an image to the User and Save it
cv2.imshow("DISPLAYING IMAGE IN RGB FORMAT",hsv)
cv2.imwrite("BGR2HSV.jpg",hsv)
#Step 5:- Wait for the user to press any key
cv2.waitKey(0)
#Step 6:- Destroy all the windows Instances
cv2.destroyAllWindows()