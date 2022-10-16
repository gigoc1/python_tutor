#https://minseob.tistory.com/m/7
import window
import cv2
import time
import win32gui

ESC_KEY=27
FRAME_RATE = 120
SLEEP_TIME = 1/FRAME_RATE

capture = window.WindowCapture("PyTrader v0.0.6",FRAME_RATE)

while True:
    start=time.time()
    frame = capture.screenshot()
    cv2.imshow("frame1",frame)
    delta= time.time()-start
    if delta <SLEEP_TIME:
        time.sleep(SLEEP_TIME-delta)
    key= cv2.waitKey(1) & 0xFF
    if key== ESC_KEY:
        break