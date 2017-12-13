"""classification"""
"""Engine mechanism"""
from functools import reduce
import pandas as pd
import pygal
def mechanism_problem():
    """about engine incluing malfunction, engine failed, technical problem, system, mechanical
fuel starvation, run out of fuel, ran out of fuel"""
    keyword_engine = ['malfunction', 'engine', 'technical problem', 'system', 'mechanical']
    keyword_fuel = ['fuel starvation', 'run out of fuel', 'ran out of fuel']
    keyword_body = ['fatigue fracture', 'airframe', 'fatigue failure', 'crack', \
    'empannage', 'fuselage', 'starboard', 'flap', 'slat', 'aileron', 'empennage', 'spoiler']
    df = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding = "ISO-8859-1")
    summary = df.Summary.tolist()
    count_dic = {'Engine problem': 0, 'Fuel starvation': 0, 'Airframe problem': 0}
    for text in summary:
        text = str(text).lower()
        text_list = text.split()
        if any(key_eng in text for key_eng in keyword_engine):
            count_dic['Engine problem'] += 1
        elif any(key_body in text for key_body in keyword_body):
            count_dic['Airframe problem'] += 1
        if any(key_fuel in text for key_fuel in keyword_fuel):
            count_dic['Fuel starvation'] += 1
        for each in text_list:
            if each in ['wheel', 'wing', 'wings']:
                count_dic['Airframe problem'] += 1
    all_mechanism_problem = count_dic['Engine problem']+count_dic['Airframe problem']+count_dic['Fuel starvation']
    return {'Mechanism': all_mechanism_problem}
"""find target 'ถูกปล้น'
HijackStat_AttackStat_SuicideStat"""
import pandas as pd
def HijStat_AttStat_SuiStat():
    """use pandas as pd
    find hijack by keyword (hijack, bomb, grenade)
    hij = hijack, at = attack, sui = suicide"""
    keywords_hij = ['hijack', 'grenade']
    specific_bomb = ['bomb', 'bomber', 'bombing']
    keyword_att = 'shot'
    keyword_sui = 'suicide'
    count_dic = {'Hijack': 0, 'Attack': 0, 'Suicide': 0}
    df = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding = "ISO-8859-1")
    summary = df.Summary.tolist()
    for text in summary:        #for any row in .csv (jsut only Summary)
        text_low = str(text).lower()
        if keyword_att in text_low:
            count_dic['Attack'] += 1
        if keyword_sui in text_low:
            count_dic['Suicide'] += 1
        text_list = str(text_low).split()      #make list() in list() cause need to check specific word
        for word in text_list:         #for word in text_list of list name 'summary'
            if word in specific_bomb:   # use for anti about another word 'bomb'does not relate such as 'bombay'
                count_dic['Hijack'] += 1
            elif any(key_hij in word for key_hij in keywords_hij):     #Let's check by keywords (each keyword)
                count_dic['Hijack'] += 1
    return count_dic
def human_error():
    """ will return 2 dict
        1.all of human error dict
        2.human error:'improper maintance and specific human error"""
    df = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding = "ISO-8859-1")
    summary = df.Summary.tolist()
    keyword = ['pilot error', 'wrong', 'crew error']
    count_dic = {'Human error': 0, 'Improper maintenance': 0}
    for text in summary:
        text = str(text).lower()
        if any(key_hum in text for key_hum in keyword): #counting by use keyword check into text
            count_dic['Human error'] += 1
        elif 'maintenance' in text or 'maintain' in text:
            count_dic['Improper maintenance'] += 1
    all_human_error = count_dic['Human error']+count_dic['Improper maintenance'] #find sum
    return {'Human Error' : all_human_error}
def all_weather(weathers):
    '''collect all wether'''
    dict_ = {'Weather':0}
    for weather in weathers.values():
        dict_['Weather'] += int(weather)
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
    dict_ = {'Geography':0}
    summary = df.Summary
    for text in summary:
        text = str(text).lower()
        lsts = str(text).split()
        for lst in lsts:
            if any(key in lst for key in specific_mount):
                dict_['Geography'] += 1
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
def main():
    '''Main Function'''
    df = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding = "ISO-8859-1")
    weathers = reduce(lambda x,y: dict(x, **y), (event_rain(df), event_storm(df),\
     event_fog(df), event_snow(df))) # Collect to 1 dictionary of weather
    geo = event_mountain(df)
    # Collect to 1 dictionary of disturbution
    disturb = reduce(lambda x,y: dict(x, **y), (event_bird(df), event_balloon(df),event_drone(df)))
    all_weathers = all_weather(weathers)
    return all_weathers, geo, {'Distrub':disturb['bird']+disturb['balloon']+disturb['drone']}
from pygal.style import RotateStyle
def chart():
    list_all = [mechanism_problem(), human_error()]
    list_lable = []
    list_val = []
    for x in HijStat_AttStat_SuiStat():
        t = {}
        t[x] = HijStat_AttStat_SuiStat()[x]
        list_all.append(t)
    for y in main():
        list_all.append(y)
    for i in list_all:
        for j in i:
            list_lable.append(j)
            list_val.append(int(i[j]))
    list_val.sort(reverse=True)
    dark_rotate_style = RotateStyle('#ff8723')
    line_chart = pygal.Bar(fill=True, interpolate='cubic', style=dark_rotate_style, x_label_rotation=30)
    line_chart.title = 'Classification by cause that affect on accident'
    line_chart.x_labels = ['Weather', 'Mechanism', 'Geography',\
     'Human Error', 'Attack', 'Hijack', 'Disturb', 'Suicie'] 
    line_chart.add('Frequency :', list_val)
    line_chart.render_to_file('bar_chart_classification.svg')                          # Save the svg to a file
chart()