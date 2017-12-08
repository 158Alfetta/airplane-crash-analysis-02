'''Getting keyword of landing and takeoff'''
import pandas as pd
from operator import itemgetter
from collections import OrderedDict
path = '/Users/punmanat/Documents/GitHub/airplane-crash-analysis-02/dataset_psit.csv'
df = pd.read_csv(path, encoding='ISO-8859-1')
def main(df):
    '''main function'''
    landing, takeoff = get_list(df)
    keyword_landing = landing_dct(df, landing)
    keyword_takeoff = takeoff_dct(df, takeoff)
    return keyword_landing, keyword_takeoff

def get_list(df):
    '''landing and takeoff'''
    landing = []
    takeoff = []
    for i in df.Summary:
        text = str(i).lower()
        if 'landing' in text:
            landing.append(text)
        elif 'takeoff' in text or 'taking off' in text or 'take off' in text:
            takeoff.append(text)
    return landing, takeoff

def landing_dct(df, landing):
    '''landing'''
    dct_landing = {}
    for i in landing:
        temp = i.split()
        for i in temp:
            if i not in dct_landing:
                dct_landing[i] = 1
            else:
                dct_landing[i] += 1
        temp = []
    sorted_x = OrderedDict(sorted(dct_landing.items(), key=itemgetter(1), reverse=True))
    return dict(sorted_x)

def takeoff_dct(df, takeoff):
    '''landing'''
    dct_takeoff = {}
    for i in takeoff:
        temp = i.split()
        for i in temp:
            if i not in dct_takeoff:
                dct_takeoff[i] = 1
            else:
                dct_takeoff[i] += 1
        temp = []
    sorted_y = OrderedDict(sorted(dct_takeoff.items(), key=itemgetter(1), reverse=True))
    return dict(sorted_y)
landing, takeoff = main(df)
