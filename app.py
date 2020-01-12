from flask import Flask, render_template,url_for,request,redirect,flash  
from werkzeug import secure_filename
import os
from fastai.basic_train import load_learner
from fastai.vision import *
from fastai.vision.image import open_image 
import warnings

warnings.filterwarnings("ignore")
UPLOAD_FOLDER = './static/image'
learn = load_learner('./model')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index2.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    print('yes')
    try:
        f = request.files['img']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    except Exception as e:
        print('cannot upload')
        print(str(e))
    try:
        #img = request.form['img']
        #print(img)
        #path = url_for('static', filename = secure_filename(img)) 
        #print(img)
        img = open_image('./static/image/'+secure_filename(f.filename))
        print(f.filename)
        
        pred_class,pred_idx,outputs = learn.predict(img)
        print(pred_class)
    except Exception as e:
        print(str(e))
    return render_template('predict.html',predict_value = pred_class ,path = f.filename)


if __name__ == '__main__':
    app.run(debug=True)
