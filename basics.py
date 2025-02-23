import cv2 as cv

# ---- Frame scaling Function ---- #
def resize(frame, scale = 0.25):
    width = int(frame.shape[1] * scale )
    height = int(frame.shape[0] * scale )

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)
# ---------------------------------#

image = resize(cv.imread('G:/Wallpapers/wp2557220-wallpaper-minion.jpg'))
cv.imshow('Minioins', image)

# ------- Converting to grey scale ------- #
grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#cv.imshow('Grey_Minioins', grey)
# ---------------------------------------- #


# --------- Bluring an Image ---------- #
Blur = cv.GaussianBlur(image, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur_Minioins', Blur)
# ------------------------------------- #

# --------- Edge Ditection ------------ #
canny = cv.Canny(Blur, 125,175)
cv.imshow('Edge Diagram', canny)
# ------------------------------------- #

# --------- Dialating ----------------- #
dialated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dialated_Minioins', dialated)
# ------------------------------------- #

# ----------- Eroding an image ---------- #
erodded = cv.erode(dialated, (7,7), iterations=3)
cv.imshow('eroded_Minioins', erodded)
# --------------------------------------- #

# -------------- Rezing an image ----------- #
rezized = cv.resize(image, (700, 700), interpolation=cv.INTER_CUBIC)
cv.imshow('resized_Minioins', rezized)
# ------------------------------------------ #

# --------------- cropping an image ----------- #
crop = image[50:600, 100:800]
cv.imshow('cropped_Minioins', crop)
# --------------------------------------------- #


cv.waitKey(0)