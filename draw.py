#draw a line on image

#Step 1: - Import the necessary packages
import cv2
# Step 2 :- Create the object to hold an image
img=cv2.imread("flower1.jpg",1)
#Step 3:- Draw the shape on the object by passing parameters
# Draw a diagonal blue line with thickness of 5 px
line=cv2.line(img,(0,0),(511,511),(300,0,0),8)# Here the parameters are objectname,starting & ending coordinate,color,thickness
#Step 4:- Display the image
cv2.imshow("Display",line)
#Step 5:- Save a image
cv2.imwrite("LINEONIMAGE.jpg",line)
#Step 6:- Clear all the things when done
cv2.waitKey(0)
cv2.destroyAllWindows()

#draw rectangle on image

# Step 1: - Import the necessary packages
import cv2
# Step 2 :- Create the object to hold an image
img=cv2.imread("flower1.jpg",1)
#Step 3:- Draw the shape on the object by passing parameters
# Drawing a green rectangle at  the mentioned coordinate with specified thickness of 3
rect=cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#Step 4:- Display the image
cv2.imshow("Display",rect)
# Step 5: Save a image
cv2.imwrite("RECTONIMAGE.jpg",rect)
#Step 6:- Clear all the things when done
cv2.waitKey(0)
cv2.destroyAllWindows()

#draw circle on image

# Step 1: - Import the necessary packages
import cv2
# Step 2 :- Create the object to hold an image
img=cv2.imread("flower1.jpg",1)
#Step 3:- Draw the shape on the object by passing parameters
# Drawing a red circle at  the mentioned coordinate with specified thickness of -1
# This will take image object ,statrting position ,radius of the circle,color and thickness
circle=cv2.circle(img,(447,63), 63, (0,0,255), -1)# it will draw a solid cirle
#Step 4:- Display the image
cv2.imshow("Display",circle)
#Step 5:- Save an image
cv2.imwrite("CIRCLEONIMAGE.jpg",circle)
# Step 6:- Clear all the things when done
cv2.waitKey(0)
cv2.destroyAllWindows()

#draw circle with specified thickness

# Step 1: - Import the necessary packages
import cv2
# Step 2 :- Create the object to hold an image
img=cv2.imread("flower1.jpg",1)
#Step 3:- Draw the shape on the object by passing parameters
# Drawing a red circle at  the mentioned coordinate with specified thickness of 2
# This will take image object ,statrting position ,radius of the circle,color and thickness
cwth=cv2.circle(img,(447,63), 63, (0,0,255), 2)# it will draw a hollow cicle of thickness 2
#Step 4:- Display the image
cv2.imshow("Display",cwth)
# STEP 5:- SAVE THE IMAGE
cv2.imwrite("CIRCLEWITHTHICKNESS.jpg",cwth)
# STEP 6:- CLEAR all the things
cv2.waitKey(0)
cv2.destroyAllWindows()

#draw ellipse

# Step 1: - Import the necessary packages
import cv2
# Step 2 :- Create the object to hold an image
img=cv2.imread("flower1.jpg",1)
#Step 3:- Draw the shape on the object by passing parameters
# The arguments passed are image object,centre location(x,y),axes length(major and minor),angle of rotation,start and
# end angle, Color,thickness
el=cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#Step 4:- Display the image
cv2.imshow("Display",el)
# STEP 5:- SAVE IMAGE
cv2.imwrite("ELLIPSEONIMAGE.jpg",el)
# STEP 6: Clear all the things when done
cv2.waitKey(0)
cv2.destroyAllWindows()

#adding text to image

# Step 1: - Import the necessary packages
import cv2
# Step 2 :- Create the object to hold an image
img=cv2.imread("flower1.jpg")
#Step 3:- Put the text on the object by passing parameters
font = cv2.FONT_HERSHEY_SIMPLEX
txt=cv2.putText(img,'OpenCV',(20,500), font, 4,(201,220,220),8,cv2.LINE_AA)#cv2.LINE_AA is for anti-aliasing.It is optional
#Step 4:- Display the image
cv2.imshow("Display",txt)
#STEP 5:- Save Image
cv2.imwrite("TEXTONIMAGE.jpg",txt)
# Step 6:- Clear all the things when done
cv2.waitKey(0)
cv2.destroyAllWindows()