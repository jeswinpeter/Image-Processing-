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

cv.rectangle(blank, (100,100), (300,300), (50,150,200), thickness=-1)
#cv.imshow('Red',blank)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40,(150,100,250), thickness=-1)

cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(150,10,250), thickness=2)
cv.imshow('Line', blank)

cv.waitKey(0)