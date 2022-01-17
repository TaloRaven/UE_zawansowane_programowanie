import cv2
import imutils
import numpy as np
from Modules.Persondetection import person_detect


if __name__ == "__main__":
    person_detect('1.jpg')
    person_detect('2.jpg')
    person_detect('3.jpg')
    person_detect('4.jpg')
