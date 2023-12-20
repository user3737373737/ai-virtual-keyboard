import cv2


BLUE = (255, 255, 0)
class Button:
    def __init__(self, text, pos, size=(50, 50)):
        self.text = text
        self.pos = pos
        self.size = size
