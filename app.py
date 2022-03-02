from flask import Flask, render_template, request
import pickle
import pandas as pd

# app instantiation
APP = Flask(__name__)

# Load model

# with open("#", "rb") as f:
#     model = pickle.load(f)


@APP.route('/')
def Home_page():
    '''Landing page to the Kickstarter Prediction project'''
    return render_template('landing.html', title='Home')

@APP.route('/prediction', methods= ["POST"])
def prediction():
    lat = request.form['lat']
    long = request.form['long']
    room_type = request.form['room_type']
    accomodates = request.form['accomodates']
    #prj_length = request.form['length']
    # ks = create_project_df(prj_name, prj_desc, prj_goal, prj_category, prj_length)
    # predify = model.predict(ks)
    # if predify == [0]:
    #     pred_result = 'an utter failure. Re-think your life, and may God have mercy on your soul.'
    # if predify == [1]:
    #     pred_result = 'a successful individual. Revel in your glory, and be kind as you stare down on those less fortunate.' 
    # return render_template('prediction.html',
    #                        title="Prediction",
    #                        prediction=pred_result)
