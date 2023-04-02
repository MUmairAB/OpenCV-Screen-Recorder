# Importing necessary libraries
import cv2
import pyautogui as pg
import numpy as np

# Capture screen resolution
resol = pg.size()
filename = r"screen_recording.mp4"

# Frames Per Second (FPS) rate of the video
fps = 30.0

# Create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(filename = filename,
                         fourcc = fourcc,
                         fps = fps,
                         frameSize = resol,
                         isColor = True)

# Create a window to show the recording
cv2.namedWindow("Video Recording",cv2.WINDOW_NORMAL)
# Resize the window
cv2.resizeWindow("Video Recording",(480,260))

while output.isOpened():
    # Capture the screenshot of the screen
    scr_shot = pg.screenshot()
    # Convert image into array
    frame = np.array(scr_shot)
    # Convert the BGR image to RGB
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # Save the image to the video file
    output.write(frame)
    # Display the video
    cv2.imshow("Video Recording", frame)
    # Stop recording when the user presses"q"
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
output.release()
