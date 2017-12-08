'''Weather'''
import pandas as pd
import pygal
from functools import reduce

#SECTION THAT IS BEING MODIFIED/ADDED.
bar_chart = pygal.Bar()
bar_chart = pygal.Bar(width=640)



#==========================   Customization section is here!   ===========================
#=====   Below are default string values, you can change to whatever that fits.   ========

Rain = 'Rain'
Storm = 'Storm'
Fog = 'Fog'
Snow = 'Snow'
Mountain = 'Mountain'
Bird = 'Bird'
Drone = 'Drone'
Balloon = 'Balloon'
Directory = 'C:\\Users\\Lert Krush\\Desktop\\clean_data_year.csv'

#========================================   END   ========================================



weatherdict = {Rain:0, Storm:0, Fog:0, Snow:0, Mountain:0, Bird:0, Drone:0, Balloon:0,}

#END.

def main():
    '''Main Function'''
    df = pd.read_csv(Directory, encoding='ISO-8859-1')
    weathers = reduce(lambda x,y: dict(x, **y), (event_rain(df), event_storm(df),\
     event_fog(df), event_snow(df))) # Collect to 1 dictionary of weather
    geo = event_mountain(df)
    # Collect to 1 dictionary of disturbution
    disturb = reduce(lambda x,y: dict(x, **y), (event_bird(df), event_balloon(df),event_drone(df)))
    all_weathers = all_weather(weathers)
    #SECTION THAT IS BEING MODIFIED/ADDED.
    global weatherdict
    text = 'Dummy'
    triggerexit = 4 #Change the total number of data type from 7 to 4 manually...
    counter = 0
    print('Processing...')
    while triggerexit > 0:
        counter+=1
        if counter%4 == 0:
            text=Rain
        elif counter%4 == 1:
            text=Storm
        elif counter%4 == 2:
            text=Fog
        elif counter%4 == 3:
            text=Snow
        if (weatherdict[text] >= weatherdict[Rain]) & (weatherdict[text] >= weatherdict[Storm]) & (weatherdict[text] >= weatherdict[Fog]) & (weatherdict[text] >= weatherdict[Snow]):
            bar_chart.add(text, [weatherdict[text]])
            weatherdict[text]=0
            triggerexit -= 1
            print('Finished processing ' + text + ' lebel. : ' + str(4-triggerexit) + '/4')
    bar_chart.render_to_file('BarChart.svg')
    print("Done!")
    #END.

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
                #SECTION THAT IS BEING MODIFIED/ADDED.
                global weatherdict
                weatherdict[Rain]+=1
                #END.

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
                #SECTION THAT IS BEING MODIFIED/ADDED.
                global weatherdict
                weatherdict[Storm]+=1
                #END.

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
                #SECTION THAT IS BEING MODIFIED/ADDED.
                global weatherdict
                weatherdict[Fog]+=1
                #END.

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
                #SECTION THAT IS BEING MODIFIED/ADDED.
                global weatherdict
                weatherdict[Snow]+=1
                #END.

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
                #SECTION THAT IS BEING MODIFIED/ADDED.
                global weatherdict
                weatherdict[Mountain]+=1
                #END.

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
                #SECTION THAT IS BEING MODIFIED/ADDED.
                global weatherdict
                weatherdict[Bird]+=1
                #END.

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
                #SECTION THAT IS BEING MODIFIED/ADDED.
                global weatherdict
                weatherdict[Drone]+=1
                #END.

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
                #SECTION THAT IS BEING MODIFIED/ADDED.
                global weatherdict
                weatherdict[Balloon]+=1
                #END.

    return dict_

main()
