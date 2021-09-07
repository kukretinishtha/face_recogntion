import cv2

faceCascade = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')

def face_detection(image_gray_scale):
    """
    This function is for face detection in image
    Args: gray scale image
    Output: return grayscale face detected stream
    """
    faces = faceCascade.detectMultiScale(image_gray_scale, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))
    for (x,y,w,h) in faces:
        roi_gray = image_gray_scale[y:y+h, x:x+w]
    return roi_gray

def similarity_check(image1, image2):
    """
    This function implements the face recognition algorithm
    Args: grayscale image stream of IMG1 and IMG2 
    Output: returns the similarity value
    """
    try:
        histogram1 = cv2.calcHist([image1], [0],None, [256], [0, 256])
        histogram2 = cv2.calcHist([image2], [0],None, [256], [0, 256])
        similarity_index = cv2.compareHist(histogram1, histogram2, cv2.HISTCMP_CORREL)
        return({"status":"success", "similarity_index":similarity_index})
    except Exception as error:
        return({"status":"failure", "msg":"image is empty"})