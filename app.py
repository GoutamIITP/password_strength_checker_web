from flask import Flask, redirect,url_for,render_template,request
import pickle
import numpy as np
from utility import check_password_strength, load_vectorizer, load_model

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

def word_divide_char(inputs):
    character = []
    for i in inputs:
        character.append(i)
    return character

 
@app.route("/predict",methods=['GET','POST'])
def predict():
    if request.method == "POST":
        exampleInputPassword1 = request.form['password']
        
         
    
    # Load the pre-trained vectorizer and model
        saved_vectorizer = load_vectorizer()
        final_model = load_model()
  
        prediction = check_password_strength(exampleInputPassword1, saved_vectorizer, final_model)
        if prediction==0:
            return render_template("index.html",strength="Password is Very Weak")
        if prediction==1:
            return render_template("index.html", strength="Average Password")
        if prediction==2:
            return render_template("index.html",strength= "Strong Password")
    else:
        return render_template('index.html')        

    
if __name__=='__main__':
    app.run(debug=True)
