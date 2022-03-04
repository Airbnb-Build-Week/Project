from flask import Flask, render_template, request
import pickle
import joblib
import pandas as pd

# app instantiation
APP = Flask(__name__)

@APP.route('/')
def Home_page():
    '''Landing page to the Kickstarter Prediction project'''
    return render_template('landing.html', title='Home')

@APP.route('/prediction', methods= ["POST"])
def prediction():
    # Winter, Spring, Summer, Fall
    time_of_year = request.form['time_of_year'] #
    # Latitude and Longitude
    lat = float(request.form['lat'])
    lon = float(request.form['lon'])
    # Room Type, Superhost, Instant Bookable, Description Length
    room_type = request.form['room_type']
    super_host = True if request.form['super_host']=='1' else False
    instant_bookable = True if request.form['instant_bookable']=='1' else False
    description_len = len(request.form['description'])
    # Accomodates, Bedrooms, Beds, Baths, Shared Baths, ppl_per_bed
    accommodates = int(request.form['accomodates']) #
    n_bedrooms = int(request.form['n_bedrooms']) #
    n_beds = int(request.form['n_beds']) #
    n_baths = int(request.form['n_baths']) #
    shared_baths = True if request.form['shared_baths']=='1' else False
    ppl_per_bed = accommodates/n_beds if n_beds!=0 else accommodates/1
    n_amenities = int(request.form['n_amenities']) #
    # Host experience, total reviews, total_statisfaction, reviews since
    host_since = int(request.form['host_since'])
    host_experience_yrs = round(2021 - int(host_since))
    total_reviews = int(request.form['total_reviews'])
    total_satisfaction = float(request.form['total_satisfaction']) # If we average the survey values then how are we going to ask 
    reviews_per_month = total_reviews/(host_experience_yrs*12)
    # Min and Max nights
    min_nights = int(request.form['min_nights'])
    max_nights = int(request.form['max_nights'])

    # Dataframe
    column_names = ['lat', 'lon', 'room_type', 'super_host', 'instant_bookable',
       'description_len', 'n_amenities', 'accommodates', 'n_bedrooms',
       'n_beds', 'n_baths', 'shared_baths', 'min_nights', 'max_nights',
       'reviews_per_month', 'total_reviews', 'total_satisfaction',
       'host_experience_yrs', 'ppl_per_bed']

    info = [[lat, lon, room_type, super_host, instant_bookable,
       description_len, n_amenities, accommodates, n_bedrooms,
       n_beds, n_baths, shared_baths, min_nights, max_nights,
       reviews_per_month, total_reviews, total_satisfaction,
       host_experience_yrs, ppl_per_bed]]

    listing = pd.DataFrame(info,columns=column_names)
    # # Choose what time of year it is
    # # Run correct model
    if time_of_year == "winter":
      model_winter = joblib.load("ModelWinter")
      pred = model_winter.predict(listing)
    elif time_of_year == "spring":
      model_spring = joblib.load("ModelSpring")
      pred = model_spring.predict(listing)
    elif time_of_year == "summer":
      model_summer = joblib.load("ModelSummer")
      pred = model_summer.predict(listing)
    elif time_of_year == "fall":
      model_fall = joblib.load("ModelFall")
      pred = model_fall.predict(listing)

    return render_template('prediction.html',
                            title='Prediction',
                            prediction=pred)