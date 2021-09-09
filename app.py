import base64
import json
from flask import Flask, request
from facerecognition import face_detection, similarity_check, convert_base64_to_image

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
    return "Hi Iam up.... Face Recogniton is running!!!!"

@app.route("/facesimilarity", methods=['GET', 'POST'])
def facesimilarity():
    if request.method == 'POST':
        if not request.data:
            return({"status":"failure", "msg":"empty data"})
        else:
            data = json.loads(request.data)
            profile_photo_data = data["profile_photo"]
            body_photo_data = data["body_photo"]
            profile_photo_data_path = convert_base64_to_image(profile_photo_data)
            body_photo_data_path = convert_base64_to_image(body_photo_data)
            profile_photo_face_detection = face_detection(profile_photo_data_path)
            body_photo_face_detection = face_detection(body_photo_data_path)
            return similarity_check(profile_photo_face_detection, body_photo_face_detection)
    else:
        return({"status":"failure", "msg":"Method not allowed"})

if __name__ =="__main__":  
    app.run(debug = True)  