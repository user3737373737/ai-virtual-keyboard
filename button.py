import cv2


BLUE = (255, 255, 0)
class Button:
    def __init__(self, text, pos, size=(50, 50)):
        self.text = text
        self.pos = pos
        self.size = size
"""
    def draw(self, img, color):
        x, y = self.pos
        w, h = self.size
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(img, self.pos, (x + w, y + h), color, cv2.FILLED)
        cv2.putText(img, self.text, (x + 8, y + 47), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
"""