# -*- coding: utf-8 -*-
"""
Created on Sat May 22 06:27:24 2021

@author: Souhardya
"""

from flask import Flask, request,render_template
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def welcome():
    bmi=''
    if request.method=='POST' and 'height' in request.form:
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        bmi =CalculateBMI(height , weight)
    return render_template('index.html',
                            bmi=bmi)

def CalculateBMI(h,w):
    bmi=(w/(h*h))*10000
    return round(bmi,2)





