import base64
import uuid
import os
import cv2
import numpy as np
import base64

faceCascade = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')

def convert_base64_to_image(base64string):
    """
    This function is used to convert base64 string into image.jpeg and returns filename
    Args: base64string
    Output: filename
    """
    if len(base64string) !=0:
        image_data = base64.b64decode(str(base64string))
        filename = os.path.join('data', str(uuid.uuid4())+'.jpg')
        decodeit = open(filename, 'wb')
        decodeit.write(image_data)
        decodeit.close()
        return filename
    else:
        return "error"
        
def face_detection(image_path):
    """
    This function is for face detection in image
    Args: gray scale image
    Output: return grayscale face detected stream
    """
    try:
        image = cv2.imread(image_path)
        image_gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(image_gray_scale, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = image_gray_scale[y:y+h, x:x+w]
            roi_color = image[y:y+h, x:x+w]
        filename = os.path.join('output', str(uuid.uuid4())+'.jpg')
        cv2.imwrite(filename, roi_gray)
        os.unlink(image_path)
        return filename
    except Exception as error:
        return error

def similarity_check(profile_photo_path, body_photo_path):
    """
    This function implements the face recognition algorithm
    Args: grayscale image stream of IMG1 and IMG2 
    Output: returns the similarity value
    """
    try:
        image1 = cv2.imread(profile_photo_path)
        image2= cv2.imread(body_photo_path)
        histogram1 = cv2.calcHist([image1], [0],None, [256], [0, 256])
        histogram2 = cv2.calcHist([image2], [0],None, [256], [0, 256])
        similarity_index = cv2.compareHist(histogram1, histogram2, cv2.HISTCMP_CORREL)
        os.unlink(profile_photo_path)
        os.unlink(body_photo_path)
        if similarity_index > 0.10:
            return({"status":"success", "similarityIndex":similarity_index})
        else:
            return({"status":"failure", "similarityIndex":similarity_index})
    except Exception as error:
        return({"status":"failure", "msg":"image is empty"})