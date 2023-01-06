import cv2
from utils.detect import detect
import imutils

class detectByPathImage:
    def __init__(path, output_path):
        image = cv2.imread(path)

        image = imutils.resize(image, width = min(800, image.shape[1])) 

        result_image = detect(image)

        if output_path is not None:
            cv2.imwrite(output_path, result_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()