import cv2
import imutils
from utils.detect import detect 
def detectByPathVideo(path,writer):
    video=cv2.VideoCapture(path)
    check,frame= video.read()
    if check ==False:
        print("video not found enter valide path")
        return
    
    print('Detecting people...')
    while video.isOpened():
        #check is true if reading was successful
        check,frame=video.read()

        if check:
            frame =imutils.resize(frame,width=min(800,frame.shape[1]))
            frame = detect(frame)
            
            if writer is not None:
                writer.write(frame)

            key=cv2.waitKey(1)
            if key== ord('q'):
                break
        else:
            break
    video.release()
    cv2.destroyAllWindows()