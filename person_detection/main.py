import cv2
import imutils
import numpy as np
from Modules.Persondetection import person_detect
import glob


def main():
    cv_img = []
    for img in glob.glob("img/*.jpg"):
        n = cv2.imread(img)
        cv_img.append(n)

    for x in cv_img:
        person_detect(x)


if __name__ == "__main__":
    main()
