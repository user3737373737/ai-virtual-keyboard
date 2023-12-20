import mediapipe as mp
import numpy as np
from time import sleep
from button import*

hand_detector = mp.solutions.hands.Hands()

cap = cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

final_txt = ''

BLUE = (255, 255, 0)
GREEN = (0, 255, 0)
flag = BLUE
xb = 0
yb = 0

Buttons = []

letters = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
           ["A", "S", "D", "F", "G", "H", "J", "K", "L", ":"],
           ["Z", "X", "C", "V", "B", "N", "M", "<", ">", "?"]]

cv2.imshow('res',cap)
cv2.waitKey(1)