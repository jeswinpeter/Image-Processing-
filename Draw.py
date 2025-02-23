import cv2 as cv
import numpy as np

# ---- Frame scaling Function ---- #
def resize(frame, scale = 0.55):
    width = int(frame.shape[1] * scale )
    height = int(frame.shape[0] * scale )

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)
# -----------------------------------#


# image = resize(cv.imread('D:/HTML CSS/IMAGES/TEST_banner.png'))
# cv.imshow('IMAGE', image)


# ------ Creating a blank window where you can work---
blank = np.zeros((600,1000,3), dtype='uint8')
# cv.imshow('Blank', blank)
# ---------------------------------------------------

blank[:] = 15,100,230


# --------- Drawing a rectangle -----------
cv.rectangle(blank, (100,100), (300,300), (50,150,200), thickness=-1)
#cv.imshow('Red',blank)
# -----------------------------------------


# ------ Drawing a Circle of radius 40 -------------
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40,(150,100,250), thickness=-1)
# --------------------------------------------------


# -------------- Drawing a line ------------
cv.line(blank, (0,500), (blank.shape[1]//2, blank.shape[0]//2),(150,10,250), thickness=2)

# ------------------------------------------


# ---------- Writing text on image -----------
cv.putText(blank, 'Bazinga', (500,200), cv.FONT_HERSHEY_DUPLEX, 1.2, (20,5,5), 2)
cv.imshow('Text', blank)
# --------------------------------------------


# -- Closes when any key is pressed -- 
cv.waitKey(0)
# ------------------------------------