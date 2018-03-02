#capture a video from camera and display it to user frame by frame
'''
#Step 1: Import the required Packages
import cv2
#Step 2:- Create a Video Capture Object to record the Video and pass the argument.
        #It takes the device index which starts from 0(0 or -1 for current  device camera and 1 for other camera device)
        #or the video file name along with its path
cap = cv2.VideoCapture('my_video.mp4')
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here. Here we are converting each frame into Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
# Destroy all the previously created window objects.
cv2.destroyAllWindows()

#play a video in slow speed

# If you set the waitKey(milliseconds) to too low the video will play very fast and if you set its duration to high the video
# will play slowly.That's how you can create a slow motion videos.
#Import the required Packages
import cv2
#Create a videoCapture object to hold the video
cap=cv2.VideoCapture("my_video.mp4")
# Return the video frames or display it to the user
while(cap.isOpened()):
    ret, frame=cap.read()
    #Display the video frames to the User
    cv2.imshow('frame',frame)
    if cv2.waitKey(2000) & 0xFF==ord('a'):
        break
#Release allthe frames
cap.release()
#Destroy all the Windows
cv2.destroyAllWindows()


#play  a video in normal speed

# If you set the waitKey(milliseconds) to too low the video will play very fast and if you set its duration to high the video
# will play slowly.That's how you can create a slow motion videos.
#Import the required Packages
import cv2
#Create a videoCapture object to hold the video
cap=cv2.VideoCapture("my_video.mp4")
# Return the video frames or display it to the user
while(cap.isOpened()):
    ret, frame=cap.read()
    #Display the video frames to the User
    cv2.imshow('frame',frame)
    if cv2.waitKey(25) & 0xFF==ord('a'):
        break
#Release allthe frames
cap.release()
#Destroy all the Windows
cv2.destroyAllWindows()

#play a video in fast speed

# If you set the waitKey(milliseconds) to too low the video will play very fast and if you set its duration to high the video
# will play slowly.That's how you can create a slow motion videos.
#Import the required Packages
import cv2
#Create a videoCapture object to hold the video
cap=cv2.VideoCapture("my_video.mp4")
# Return the video frames or display it to the user
while(cap.isOpened()):
    ret, frame=cap.read()
    #Display the video frames to the User
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('a'):
        break
#Release allthe frames
cap.release()
#Destroy all the Windows
cv2.destroyAllWindows()

#saving a video

# Step 1:-  Import the required packages
import cv2
# Step 2:-  Create a video Capture  object  to hold the video
cap = cv2.VideoCapture(0) #This capture the video from the Camera
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID') #The fourcc is used to mention the video codec for encoding the video
#The VideoWriter() accepts four parameters.These are as follows:
    # 1) The output file name along with the format in which you want to save the file
    # 2) The video codec or fourcc.
    # 3) Frames per second which is used to mention how fast or slow your video should play along with the frame size that is the size of the window
    # 4) isColor flag. If it is True, encoder expect color frame, otherwise it works with grayscale frame.
out = cv2.VideoWriter('webcam.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))), isColor=True)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

'''
#convert video into grayscale and display to user

#Step 1:- Import the required packages
import cv2
#Step 2:- Create a VideoCapture object to hold the video in it
cap=cv2.VideoCapture(0)# Capturing video from the camera
# Step 3: Displaying it to the user
while(cap.isOpened()):
    ret, frame=cap.read()
    #Step 4: Perform Color Inversion on the frames
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Step 5:- Displaying it to the user
    cv2.imshow("DISPLAY",gray)
    #Step 6: Checking for user's interaction  with keyboard
    if cv2.waitKey(25) & 0xFF==ord('a'):#Exit whenever user press the a key on the keyboard
        break
#Step 7: Releasing everything after the job is done
cap.release()
cv2.destroyAllWindows()

#convert video in RGB format

#Step 1:- Import the required packages
import cv2
#Step 2:- Create a VideoCapture object to hold the video in it
cap=cv2.VideoCapture(0)# Capturing video from the camera
# Step 3: Displaying it to the user
while(cap.isOpened()):
    ret, frame=cap.read()
    #Step 4: Perform Color Inversion on the frames
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)#This will convert BGR to RGB
    #Step 5:- Displaying it to the user
    cv2.imshow("DISPLAY",gray)
    #Step 6: Checking for user's interaction  with keyboard
    if cv2.waitKey(25) & 0xFF==ord('a'):#Exit whenever user press the a key on the keyboard
        break
#Step 7: Releasing everything after the job is done
cap.release()
cv2.destroyAllWindows()


#display video in HSV format

#Step 1:- Import the required packages
import cv2
#Step 2:- Create a VideoCapture object to hold the video in it
cap=cv2.VideoCapture(0)# Capturing video from the camera
# Step 3: Displaying it to the user
while(cap.isOpened()):
    ret, frame=cap.read()
    #Step 4: Perform Color Inversion on the frames
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#This will convert BGR into HSV format
    #Step 5:- Displaying it to the user
    cv2.imshow("DISPLAY",gray)
    #Step 6: Checking for user's interaction  with keyboard
    if cv2.waitKey(25) & 0xFF==ord('a'):#Exit whenever user press the a key on the keyboard
        break
#Step 7: Releasing everything after the job is done
cap.release()
cv2.destroyAllWindows()


#saving video in different format

# Step 1:- Import the required packages
import cv2

# Step 2:- Create a VideoCapture object to capture the video
cap = cv2.VideoCapture("webcam.avi")  # COSTA.mp4 is the filename of the video along with the format name
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # For fourcc visit fourcc.org

# using isColor = False to save gray scale video
out = cv2.VideoWriter('ConvertedVideo.avi', fourcc, 20, (int(cap.get(3)), int(cap.get(4))), isColor=False)

# Step 3: Return the video frame by frame
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # Step 4:- Displaying it to the user after performing color inversion
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Step 5:- Write the file into the disk with specific format
        out.write(gray)
        cv2.imshow("DIPLAYING TO USER", gray)
        if cv2.waitKey(25) & 0xFF == ord('a'):
            break
    else:
        break
# Step 6 : Release everything after use
cap.release()
out.release()
cv2.destroyAllWindows()