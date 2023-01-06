import cv2
from utils.detect import detect

class detectByCamera:
    def __init__(writer):   
        video = cv2.VideoCapture(0)
        print('Detecting people...')

        while True:
            check, frame = video.read()

            frame = detect(frame)
            if writer is not None:
                writer.write(frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                    break

        video.release()
        cv2.destroyAllWindows()
