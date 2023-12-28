import cv2

from Cir_Detect import Detect_Circuit
import time

def show_camera():
    # Open the default camera (usually the webcam)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If the frame is read correctly, ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting...")
            break

        frame = Detect_Circuit(frame)[0]
        cv2.imshow('Video', frame)
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

# Call the function to show the camera feed


show_camera()

frame = cv2.imread('img1.jpg')
frame = Detect_Circuit(frame)[0]

start_time = time.time()
end_time = time.time()
elapsed_time_seconds = end_time - start_time
elapsed_time_milliseconds = elapsed_time_seconds * 1000
print("Elapsed time in milliseconds:", elapsed_time_milliseconds)
cv2.imshow('Video', frame)
cv2.waitKey(0)

