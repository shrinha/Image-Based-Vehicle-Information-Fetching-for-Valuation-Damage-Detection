from flask import Flask, render_template, request
import os
from deeplearning import OCR,severity_estimator
from test import fetchInfo
import tensorflow as tf
#webserver gateway interface
app = Flask(__name__)

model1 = tf.keras.models.load_model('./static/models/ft_model.h5')
BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(BASE_PATH,'static/upload/')
UPLOAD_PATH2 = os.path.join(BASE_PATH,'static/damage/')

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        upload_file = request.files['image_name']
        filename = upload_file.filename
        path_save = os.path.join(UPLOAD_PATH,filename)
        upload_file.save(path_save)
        text = OCR(path_save,filename)
        n_text = text.replace(" ","")
        print(n_text)
        nw_text = n_text.lower()
        print(nw_text)
        information = fetchInfo(nw_text)
        # print(information)
        return render_template('index.html',upload=True,upload_image=filename,info=information)

    return render_template('index.html',upload=False)

@app.route('/damage',methods=['POST','GET'])
def ind():
    if request.method == 'POST':
        upload_file = request.files['image_name']
        filename = upload_file.filename
        path_save = os.path.join(UPLOAD_PATH2,filename)
        upload_file.save(path_save)
        dmg = severity_estimator(path_save,model1)
        return render_template('index2.html',upload=True,upload_image=filename,msg=dmg)

    return render_template('index.html',upload=False)

if __name__ == "__main__":
    app.run(debug=True)