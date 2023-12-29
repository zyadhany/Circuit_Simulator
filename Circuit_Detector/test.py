import cv2

from Cir_Detect import Detect_Circuit
import time

def init():
    img = cv2.imread('img_test/img1.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    casc = cv2.CascadeClassifier('set/res.xml')
    opj = casc.detectMultiScale2(img,scaleFactor=1.05, minNeighbors=60)

def show_camera():
    # Open the default camera (usually the webcam)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        start = time.time()
        
        frame = Detect_Circuit(frame)[0]
        
        end = time.time()
        cv2.imshow('Video', frame)
        print("Time Taken: ", end - start)

        if cv2.waitKey(1) == ord('q'):
            break
        continue
        start_time = time.time()

        end_time = time.time()
        elapsed_time_seconds = end_time - start_time
        elapsed_time_milliseconds = elapsed_time_seconds * 1000
        print("Elapsed time in milliseconds:", elapsed_time_milliseconds)
        
        # Display the frame in a window named 'Video'


        # Wait for the 'q' key to be pressed to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

def show_image():
    frame = cv2.imread('img1.jpg')
    frame = Detect_Circuit(frame)[0]
    #cv2.imshow('Video', frame)
    cv2.waitKey(0)

init()
start = time.time()

show_camera()
show_image()

end = time.time()
print(end - start)
