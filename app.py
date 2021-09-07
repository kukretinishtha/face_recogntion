import base64
import traceback
from flask import Flask, request

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
    return "hi Iam up.... Face Recogniton is running!!!!"

@app.route("/facesimilarity", methods=['GET', 'POST'])
def facesimilarity():
    if not request.data:
        return({"status":"failure", "msg":"empty data"})
    else:
        print(request.data)
        return({"status":"success", "msg":"{request.data}"})
        
    