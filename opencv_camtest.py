# check camera functionality using opencv
import sys
import cv2

def camera(w=320, h=240):
    cap = cv2.VideoCapture(0)
    cap.set(3, w)
    cap.set(4, h)

    while True:
        ret, frame = cap.read()
        cv2.imshow('camera test', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) == 3:
        w = sys.argv[1]
        h = sys.argv[2]
        camera(int(w), int(h))
    else:
        camera()

