import base64

def convert_image_to_base64(image):
    """
    This function converts image to base64
    Args: Input image
    Output: returns a base64 string
    """
    try:
        data = image.read()
        if len(data) == 0:
            return("status":"failure", "msg":"Its an empty image")
        else:
            return("status":"success", "data":base64.b64encode(data))
    except Exception as error:
        return("status":"success", "msg":error)

def convert_base64_to_image(imagebase64):
    """
    This function converts base64 to image
    Args: Input base64
    Output: returns a image
    """
    try:
        data = image.read()
        if len(data) == 0:
            return("status":"failure", "msg":"Its an empty image")
        else:
            return("status":"success", "data":base64.b64encode(data))
    except Exception as error:
        return("status":"success", "msg":error)

def image_read(image_path):
    """
    This function is read image
    Args: input imape path
    output: return a stream of data
    """
    try:
        if os.path.join(image_path):
            image = cv2.imread(image_path)
            return image
        else:
            return({"status":"failure", "msg":"image file does not exist"})
    except Exception as error:
        return({"status":"failure", "msg": error})

def image_to_gray_scale(image):
    """
    This function is to convert image into gray scaale
    Args: Image is the input
    Output: return a gray scale image 
    """
    try:
        if len(image)>0:
            return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            return({"status":"failure", "msg":"image is an empty file"})
    except Exception as error:
        return({"status":"failure", "msg": error})