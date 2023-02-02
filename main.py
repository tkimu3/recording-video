from selenium import webdriver
import cv2
import numpy as np
import pyautogui as pg

# Create a Chrome driver instance
options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-gpu-sandbox')
options.add_argument('--disable-setuid-sandbox')

# driver = webdriver.Chrome(chrome_options=options)

# # # Open a URL in Chrome
# url = "https://www2.nhk.or.jp/gogaku/gendaieigo/detail/video.html?no=20230126&file=22-3508-184&thumb=22-3508-184.jpg"
# driver.get(url)

# Get the size of the screen
# w = driver.execute_script("return window.innerWidth")
# h = driver.execute_script("return window.innerHeight")

w = 2560
h = 1440


# # Get the screen as a video stream
# cap = cv2.VideoCapture(0)
# cap.set(3, w)
# cap.set(4, h)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('output.mp4', fourcc, 20.0, (int(w), int(h)))

while True:
    # ret, frame = cap.read()
    # if ret == True:
    #     # write the frame
    #     video.write(frame)

    #     cv2.imshow('frame', frame)

    # take a screenshot
    # This code is from https://www.youtube.com/watch?v=2mvdhuGskyA

    screenshot = cv2.cvtColor(np.array(pg.screenshot()), cv2.COLOR_RGB2BGR)

    # display screenshot in a window
    # cv2.imshow('Screenshot', screenshot)

    # write video frame
    video.write(screenshot)

    # escape condition (stop when pressing Esc)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # else:
    #     break

# Release everything if job is finished
#cap.release()
video.release()
cv2.destroyAllWindows()
# driver.close()