from flask import Flask, render_template, escape, request,jsonify
from functions import get_trending, get_tweets,get_top_10, prepare_top_10
#import pandas as pd
import logging
import json

logging.basicConfig(filename='info.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S' ,level=logging.INFO)
app= Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def root():
    return render_template('base.html')

@app.route('/predict')
def predict():
    result = prepare_top_10()
    return jsonify(result)
