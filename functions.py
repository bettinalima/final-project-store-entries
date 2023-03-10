import datetime

def week_day_to_num(week_day):
    if week_day == "Sunday":
        return 1
    if week_day == "Monday":
        return 2
    if week_day == "Tuesday":
        return 3
    if week_day == "Wednesday":
        return 4
    if week_day == "Thursday":
        return 5
    if week_day == "Friday":
        return 6
    if week_day == "Saturday":
        return 7
    

def get_date(date_input):
    date = date_input.split("-")
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])

    d = datetime.datetime(year,month,day).weekday() #returns a number from 0-6
    day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    day_of_the_week = day_list[d]

    if day_of_the_week == "Sunday":
        day_of_the_week_num = 1
    if day_of_the_week == "Monday":
        day_of_the_week_num = 2
    if day_of_the_week == "Tuesday":
        day_of_the_week_num = 3
    if day_of_the_week == "Wednesday":
        day_of_the_week_num = 4
    if day_of_the_week == "Thursday":
        day_of_the_week_num = 5
    if day_of_the_week == "Friday":
        day_of_the_week_num = 6
    if day_of_the_week == "Saturday":
        day_of_the_week_num = 7

    #day_of_the_week_num = week_day_to_num(day_of_the_week) #So the value matches the one we passed to our algorithm
    return str(day), str(month), year, day_of_the_week_num


def get_season(season_name):
    season = season_name.lower()

    if season == "autumn":
        season_autumn = 1
        season_spring = 0
        season_summer = 0
        season_winter = 0
    if season == "spring":
        season_autumn = 0
        season_spring = 1
        season_summer = 0
        season_winter = 0
    if season == "summer":
        season_autumn = 0
        season_spring = 0
        season_summer = 1
        season_winter = 0
    if season == "winter":
        season_autumn = 0
        season_spring = 0
        season_summer = 0
        season_winter = 1
    
    return season_autumn,season_spring,season_summer,season_winter


def get_covid(year):
    if year >= 2020: 
        covid = 1
    else:
        covid = 0
    
    return covid


def get_event(y_or_n):
    y_or_n = y_or_n.lower()
    if y_or_n == "yes":
        return 1
    else:
        return 0



import joblib

model = joblib.load('store_rf_model.joblib')

