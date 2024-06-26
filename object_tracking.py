import cv2
import time
import math

p1 = 530
p2 = 300



video = cv2.VideoCapture("bb3.mp4")

# Load tracker 
tracker = cv2.TrackerCSRT_create()

# Read the first frame of the video
returned, img = video.read()

# Select the bounding box on the image
bbox = cv2.selectROI("Tracking", img, False)

# Initialise the tracker on the img and the bounding box
tracker.init(img, bbox)

print(bbox)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)

    
#define goal_track function

    #Get x,y,w,h of bounding box
    

    # Get the CENTER Points of the Bounding Box
   

    # Draw a small circle using CENTER POINTS
   

  

    # Calculate Distance
    

    # Goal is reached if distance is less than 20 pixel points
   

  

   

while True:
    
    check, img = video.read()   

    # Update the tracker on the img and the bounding box
    success, bbox = tracker.update(img)

    # Call drawBox()
    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img,"Lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    # Call goal_track()
   

    # Display Video
    cv2.imshow("result", img)


    # Quit Display Window when Spacebar key is pressed        
    key = cv2.waitKey(25)
    if key == 32:
        print("Stopped")
        break

video.release()
cv2.destroyALLwindows()