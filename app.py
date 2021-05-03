from flask import Flask
from flask import render_template
import sys
from flask import request,redirect
import os
from ocr_core import ocr_core

app = Flask(__name__)

UPLOAD_FOLDER='/static/uploads/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
ALLOWED_EXTENTION=set(['png','jpg','jpeg'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENTION
@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='POST':
        if 'file' not in request.files:
            return render_template('index.html',msg="No file selected")
        xfile=request.files['file']
        if xfile.filename=='':
            return render_template("index.html",msg='No file selected')
        print(allowed_file(xfile.filename))
        if xfile and allowed_file(xfile.filename):
            print(allowed_file(xfile.filename))
            extracted_text=ocr_core(xfile)
            print("manoj    ji")
            image_src=os.path.join(app.config['UPLOAD_FOLDER'], xfile.filename)
            return render_template('index.html',msg="Successfully processed",
                                    extracted_text=extracted_text,
                                    image_src=image_src)
        else:
            return render_template("index.html",msg="Choose Valid File")

    
    else:
        return render_template("index.html")

# if __name__=='__main__':
#     app.run()
