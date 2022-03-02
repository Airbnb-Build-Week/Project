from flask import Flask, render_template, request
import pickle
import pandas as pd

# app instantiation
APP = Flask(__name__)

# Load model
#with open("xgb_class_1.pkl", "rb") as f:
 #   model = pickle.load(f)

#def create_project_df(name, blurb, goal, category, length):
    # function to process user input and make a dataframe

    # list all columns needed for model
 #   cols = ['goal', 'name_len', 'blurb_len', 'category_academic',
  #          'category_apps', 'category_blues', 'category_comedy', 
   #         'category_experimental', 'category_festivals', 'category_flight', 
    #        'category_gadgets', 'category_hardware', 'category_immersive', 
     #       'category_makerspaces', 'category_musical', 'category_places', 
      #      'category_plays', 'category_restaurants', 'category_robots', 
       #     'category_shorts', 'category_software', 'category_sound', 
        #    'category_spaces','category_thrillers', 'category_wearables', 
         #   'category_web','category_webseries', 'campaign_length_days']

 #   nlen = len(name.split())
  #  blen = len(blurb.split())
  #  cat = "category_" + category.lower()

    # Create a dataframe with 1 row with only 0's
#    ks = pd.DataFrame(columns = cols)
#    ks.loc[len(ks.index)] = 0

    # Add our variables to the dataframe
 #   ks['goal'] = int(goal)
 #   ks['name_len'] = int(nlen)
  #  ks['blurb_len'] = int(blen)
 #   ks['campaign_length_days'] = int(length)

    # "OneHotEncode" our category
  #  for col in ks.columns:
   #     if cat == col:
    #        ks[col] = 1

    #return ks

@APP.route('/')
def Home_page():
    '''Landing page to the Kickstarter Prediction project'''
    return render_template('landing.html', title='Home')

#@APP.route('/prediction', methods= ["POST"])
#def prediction():
 #   prj_name = request.form['prj']
  #  prj_desc = request.form['blurb']
   # prj_goal = request.form['goal']
    #prj_category = request.form['category']
    #prj_length = request.form['length']
    #ks = create_project_df(prj_name, prj_desc, prj_goal, prj_category, prj_length)
    #predify = model.predict(ks)
    #if predify == [0]:
    #    pred_result = 'no bueno.'
    #if predify == [1]:
    #    pred_result = 'a successful individual. Revel in your glory.' 
    #return render_template('prediction.html',
     #                      title="Prediction",
      #                     prediction=pred_result)
