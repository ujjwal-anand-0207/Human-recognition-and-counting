import cv2
import numpy as np
from imutils.object_detection import non_max_suppression


HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

class detect:
    def __init__(frame):
        bounding_box_cordinates, weights =  HOGCV.detectMultiScale(frame, winStride = (4, 4), padding = (1,1), scale = 1.03)
        bounding_box_cordinates = np.array( [[x,y,x+w,y+h]for (x,y,w,h)in bounding_box_cordinates ] )
        pick = non_max_suppression(bounding_box_cordinates, probs=None, overlapThresh=0.35)
        person = 1
        for x,y,w,h in pick:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(frame, f'person {person}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
            person += 1
        
        cv2.putText(frame, 'Status : Detecting ', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
        cv2.putText(frame, f'Total Persons : {person-1}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
        cv2.imshow('output', frame)

        return frame