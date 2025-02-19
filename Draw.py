import cv2 as cv
import numpy as np

# ---- Frame scaling Function ---- #
def resize(frame, scale = 0.55):
    width = int(frame.shape[1] * scale )
    height = int(frame.shape[0] * scale )

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


# image = resize(cv.imread('D:/HTML CSS/IMAGES/TEST_banner.png'))
# cv.imshow('IMAGE', image)

blank = np.zeros((600,1000,3), dtype='uint8')
# cv.imshow('Blank', blank)

blank[:] = 15,100,230
# cv.imshow('Red',blank)

cv.rectangle(blank, (10,10), (250,300), (50,150,200), thickness=4)
cv.imshow('Red',blank)

cv.waitKey(0)