import cv2 as cv

# ---- Frame scaling Function ---- #
def resize(frame, scale = 0.5):
    width = int(frame.shape[1] * scale )
    height = int(frame.shape[0] * scale )

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)
    

# ---- Image Reading ---- #

img = resize(cv.imread('D:/HTML CSS/IMAGES/minions_image.jpg'))

cv.imshow('minions', img)
cv.waitKey(0)


# --- Viedeo Reading --- #

capture = cv.VideoCapture('A:/Download/Manichithra thazhu thilakan dialogues.mp4')

while True:
    isTrue, frame = capture.read()

    new_frame = resize(frame)
    cv.imshow('Video', frame)
    cv.imshow('New Frame', new_frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()