from flask import Flask, render_template, request
import functions as funk
import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor

model = joblib.load('store_rf_model.joblib')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the data from the form
        input1 = request.form['date']
        input2 = request.form['season']
        input3 = request.form['event']
        input4 = request.form['tourists']
        # Do something with the data, like save it to a database

        day, month,year, day_of_the_week_num = funk.get_date(input1)
        season_autumn,season_spring,season_summer,season_winter = funk.get_season(input2)
        covid = funk.get_covid(year)
        event = funk.get_event(input3)
        tourists = float(input4)
        pred_var = np.array([day,month,covid,event,tourists,day_of_the_week_num,season_autumn,season_spring,season_summer,season_winter])
        pred_var = pred_var.reshape(1,-1)
        #print(pred_var)
        pred = model.predict(pred_var)
        #return day, month,year, day_of_the_week_num
        results = str(pred[0])
        return render_template('results.html',results=results)
        # Render the template with the input fields
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)