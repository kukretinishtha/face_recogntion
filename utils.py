import base64
import uuid
import json
import os
import io
from PIL import Image
import cv2
import numpy as np

# def convert_image_to_base64(image):
#     """
#     This function converts image to base64
#     Args: Input image
#     Output: returns a base64 string
#     """
#     try:
#         data = image.read()
#         if len(data) == 0:
#             return({"status":"failure", "msg":"Its an empty image"})
#         else:
#             return({"status":"success", "data":base64.b64encode(data)})
#     except Exception as error:
#         return({"status":"success", "msg":error})

def convert_base64_to_grayimage(imagebase64):
    """
    This function converts base64 to gray image
    Args: Input base64
    Output: returns a binary gray image
    """
    try:
        if len(imagebase64) == 0:
            return({"status":"failure", "msg":"Its an empty image"})
        else:
            image_data = base64.b64decode(str(imagebase64))
            # print(image_data)
            image = Image.open(io.BytesIO(image_data))
            # print(np.array(image))
            data = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
            # print(image)
            return({"status":"success", "image":"ok"})
    except Exception as error:
        return error

# def image_read(image_path):
#     """
#     This function is read image
#     Args: input imape path
#     output: return a stream of data
#     """
#     try:
#         if os.path.join(image_path):
#             image = cv2.imread(image_path)
#             return image
#         else:
#             return({"status":"failure", "msg":"image file does not exist"})
#     except Exception as error:
#         return({"status":"failure", "msg": error})

# def image_to_gray_scale(image):
#     """
#     This function is to convert image into gray scaale
#     Args: Image is the input
#     Output: return a gray scale image 
#     """
#     try:
#         if len(image)>0:
#             return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         else:
#             return({"status":"failure", "msg":"image is an empty file"})
#     except Exception as error:
#         return({"status":"failure", "msg": error})


def data_loader(data):
    """
    This function is used to accept the raw data from from the api
    Args: None
    Output: get the data and returns the grayscale image stream
    """
    data = json.loads(data)
    # print(data)
    if data["profile_photo"] and data["body_photo"]:
        profile_photo_data = convert_base64_to_grayimage(data["profile_photo"])
        body_photo_data = convert_base64_to_grayimage(data["body_photo"])
        return({"status": "success", "profile_photo_data": profile_photo_data, "body_photo_data":body_photo_data})
    else:
        return({"status" : "failure", "msg": "parameter is missing"})