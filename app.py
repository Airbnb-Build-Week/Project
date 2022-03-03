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

@APP.route('/', methods= ["POST"])
def prediction():
    # Winter, Spring, Summer, Fall
    time_of_year = request.form['time_of_year'] #
    # Latitude and Longitude
    lat = request.form['lat']
    lon = request.form['lon']
    # Room Type, Superhost, Instant Bookable, Description Length
    room_type = request.form['room_type']
    super_host = request.form['superhost']
    instant_bookable = request.form['instant_bookable']
    description_len = request.form['description_len']
    # Accomodates, Bedrooms, Beds, Baths, Shared Baths, ppl_per_bed
    accomodates = int(request.form['accomodates']) #
    n_bedrooms = request.form['n_bedrooms'] #
    n_beds = request.form['n_beds'] #
    n_baths = request.form['n_baths'] #
    shared_baths = request.form['shared_baths'] #
    ppl_per_bed = accomodates/n_beds if n_beds!=0 else accomodates/1
    n_amenities = request.form['n_amenities'] #
    # Host experience, total reviews, total_statisfaction, reviews since
    host_since = request.form['host_since']
    host_experience_yrs = round(2021 - int(host_since))
    total_reviews = request.form['total_reviews']
    total_statisfaction = request.form['total_satisfaction'] # If we average the survey values then how are we going to ask 
    reviews_per_month = total_reviews/(host_experience_yrs*12)
    # Min and Max nights
    min_nights = request.form['min_nights']
    max_nights = request.form['max_nights']

    print(accomodates)


    return render_template('landing.html')
