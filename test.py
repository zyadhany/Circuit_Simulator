import cv2
import pyautogui
import numpy as np
from Circuit_Detector import *
import time


cnt = 0
took = 0

def init():
	img = cv2.imread('img_test/img1.jpg')
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	casc = cv2.CascadeClassifier('set/res.xml')
	opj = casc.detectMultiScale2(img,scaleFactor=1.05, minNeighbors=60)

def FPS(s):
	global took
	global cnt
	took += time.time() - s
	cnt += 1
	print(took)
	if took >= 1:
		print(cnt / took)
		cnt = 0
		took = 0

def show_camera():
	cap = cv2.VideoCapture('Circuit_Detector/img_test/vid3.mp4')

	while True:
		ret, frame = cap.read()

		start = time.time()  
		frame = Detect_Circuit(frame)['gray']
		end = time.time()
		print("Time Taken: ", end - start)

		cv2.imshow('Video', frame)
		if cv2.waitKey(1) == ord('q'):
			break


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

def show_screen():
    screen_width, screen_height = pyautogui.size()

    start_time = time.time()
    frame_count = 0

    while True:
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        w = frame.shape[0] // 2

        s = time.time()
        frame = Detect_Circuit(frame)[0]
        cv2.imshow('Screen', frame)
        e = time.time()

        frame_count += 1

        # Calculate time taken for each frame
        elapsed_time = e - s
        #print("Time Taken for Frame {}: {:.2f} seconds".format(frame_count, elapsed_time))

        if cv2.waitKey(1) == ord('q'):
            break

    end_time = time.time()
    total_time = end_time - start_time
    fps = frame_count / total_time
    print("Average FPS: {:.2f}".format(fps))

    cv2.destroyAllWindows()


start = time.time()
show_camera()
#show_image()
#show_screen()
end = time.time()
print(end - start)
