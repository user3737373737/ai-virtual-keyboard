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

def DrawButtons(img, list1, color, xb, yb, letter):
    out = img.copy()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.rectangle(img, (xb, yb), (xb + 50, yb + 50), color, cv2.FILLED)
    cv2.putText(img, letter, (xb + 8, yb + 47), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    alpha = 0.5
    new = cv2.addWeighted(out, alpha, img, 1 - alpha, 0)
    #cv2.imshow('es', new)


for i in range(len(letters)):
    for j, l in enumerate(letters[i]):
        Buttons.append(Button(letters[i][j], [58 * j + 60, 58 * i + 60]))


while(cap.isOpened()):
    ret, frame = cap.read()
    cap_flip = np.fliplr(frame)
    cap_flip_rgb = cv2.cvtColor(cap_flip, cv2.COLOR_BGR2RGB)
    result = hand_detector.process(cap_flip_rgb)


    if result.multi_hand_landmarks is not None:
        mp.solutions.drawing_utils.draw_landmarks(cap_flip_rgb, result.multi_hand_landmarks[0], mp.solutions.hands.HAND_CONNECTIONS)
        finger_tip_x = int(result.multi_hand_landmarks[0].landmark[8].x * cap_flip_rgb.shape[1])
        finger_tip_y = int(result.multi_hand_landmarks[0].landmark[8].y * cap_flip_rgb.shape[0])

        mid_finger_tip_x = int(result.multi_hand_landmarks[0].landmark[12].x * cap_flip_rgb.shape[1])
        mid_finger_tip_y = int(result.multi_hand_landmarks[0].landmark[12].y * cap_flip_rgb.shape[0])

        cv2.circle(cap_flip_rgb, (finger_tip_x, finger_tip_y), 7, (0, 0, 0), -1)
        cv2.circle(cap_flip_rgb, (mid_finger_tip_x, mid_finger_tip_y), 7, (0, 0, 0), -1)

        finger_x = result.multi_hand_landmarks[0].landmark[8].x
        finger_y = result.multi_hand_landmarks[0].landmark[8].y
        mid_finger_x = result.multi_hand_landmarks[0].landmark[12].x
        mid_finger_y = result.multi_hand_landmarks[0].landmark[12].y

        for button in Buttons:
            x, y = button.pos
            w, h = button.size
            txt = button.text
            if x < finger_x * width < x + w and y < finger_y * height < y + h and x < mid_finger_x * width < x + w and y < mid_finger_y * height < y + h:
                final_txt += button.text
                sleep(0.07)
                flag = GREEN
                c = GREEN
                xb = x
                yb = y

    res_cap = cv2.cvtColor(cap_flip_rgb, cv2.COLOR_RGB2BGR)
    for button in Buttons:
        let = button.text
        a, b = button.pos
        w1, h1, = button.size
        if flag == GREEN and a == xb and b == yb:
            DrawButtons(res_cap, Buttons, GREEN, a, b, let)
            flag = BLUE
        else:
            DrawButtons(res_cap, Buttons, BLUE, a, b, let)
    print(final_txt)
    cv2.waitKey(1)
    cv2.imshow('frame', res_cap)
hand_detector.close()
cv2.destroyAllWindows()