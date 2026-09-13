# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:33:44 2020

@author: SHYLAJA S
"""
import os
from flask import Flask, render_template, request
import pandas as pd
import csv
from oper import operation as op

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def data():
    if request.method == 'POST':
        file = request.form['upload-file']
        #data = pd.read_excel(file).values.tolist()
        data = pd.read_excel(file)
        op(data)
        return render_template('index1.html')


if __name__ == '__main__':
    app.run(debug=True)
 