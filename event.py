'''Weather'''
import pandas as pd
from functools import reduce
def main():
    '''Main Function'''
    df = pd.read_csv('/Users/punmanat/Desktop/Project_psit/clean_data_year.csv', encoding='ISO-8859-1')
    weathers = reduce(lambda x,y: dict(x, **y), (event_rain(df), event_storm(df),\
     event_fog(df), event_snow(df))) # Collect to 1 dictionary of weather
    geo = event_mountain(df)
    # Collect to 1 dictionary of disturbution
    disturb = reduce(lambda x,y: dict(x, **y), (event_bird(df), event_balloon(df),event_drone(df)))
    all_weathers = all_weather(weathers)

def all_weather(weathers):
    '''collect all wether'''
    dict_ = {'weather':0}
    for weather in weathers.values():
        dict_['weather'] += int(weather)
    return dict_

def event_rain(df):
    '''Plane crash from rain'''
    specific_rain = ['rain', 'raining', 'hail', 'thunder']
    dict_ = {'rain':0}
    summary = df.Summary # Get column summary
    for text in summary:
        text = str(text).lower()
        lsts = str(text).split()
        for lst in lsts:
            if any(key in lst for key in specific_rain):
                dict_['rain'] += 1

    return dict_

def event_storm(df):
    '''Plane crash from storm'''
    specific_storm = ['storm', 'thunderstorm', 'gale', 'hurricane', 'tempest', 'windy']
    dict_ = {'storm':0}
    summary = df.Summary
    for text in summary:
        text = str(text).lower()
        lsts = str(text).split()
        for lst in lsts:
            if any(key in lst for key in specific_storm):
                dict_['storm'] += 1

    return dict_

def event_fog(df):
    '''Plane crash from fog'''
    specific_fog = ['fog', 'foggy', 'hazy', 'cloudy', 'mist', 'haze']
    dict_ = {'fog':0}
    summary = df.Summary
    for text in summary:
        text = str(text).lower()
        lsts = str(text).split()
        for lst in lsts:
            if any(key in lst for key in specific_fog):
                dict_['fog'] += 1

    return dict_

def event_snow(df):
    '''Plane crash from snow'''
    specific_snow = ['snow', 'sleet']
    dict_ = {'snow':0}
    summary = df.Summary
    for text in summary:
        text = str(text).lower()
        lsts = str(text).split()
        for lst in lsts:
            if any(key in lst for key in specific_snow):
                dict_['snow'] += 1

    return dict_

def event_mountain(df):
    '''Plane crash from mountain'''
    specific_mount = ['mountain', 'hill']
    dict_ = {'mountain':0}
    summary = df.Summary
    for text in summary:
        text = str(text).lower()
        lsts = str(text).split()
        for lst in lsts:
            if any(key in lst for key in specific_mount):
                dict_['mountain'] += 1

    return dict_

def event_bird(df):
    '''Plane crash from mountain'''
    specific_bird = ['bird']
    dict_ = {'bird':0}
    summary = df.Summary
    for text in summary:
        text = str(text).lower()
        lsts = str(text).split()
        for lst in lsts:
            if any(key in lst for key in specific_bird):
                dict_['bird'] += 1

    return dict_

def event_drone(df):
    '''Plane crash from mountain'''
    specific_drone = ['drone']
    dict_ = {'drone':0}
    summary = df.Summary
    for text in summary:
        text = str(text).lower()
        lsts = str(text).split()
        for lst in lsts:
            if any(key in lst for key in specific_drone):
                dict_['drone'] += 1

    return dict_

def event_balloon(df):
    '''Plane crash from mountain'''
    specific_balloon = ['balloon']
    dict_ = {'balloon':0}
    summary = df.Summary
    for text in summary:
        text = str(text).lower()
        lsts = str(text).split()
        for lst in lsts:
            if any(key in lst for key in specific_balloon):
                dict_['balloon'] += 1

    return dict_

main()