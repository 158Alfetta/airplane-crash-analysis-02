'''Getting keyword of landing and takeoff'''
import pandas as pd
from operator import itemgetter
from collections import OrderedDict
import pygal
path = 'C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv'
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
    #print(dict(sorted_y))
def count_land_take(df):
    '''Counting landing and takeoff'''
    #เอา keyword มาเก็บใน list และค่าของแต่ละคำเก็บไว้อีกตัวแปร
    landing, takeoff = main(df)
    key_landing = ['weather', 'fog', 'rain', 'stalled', 'engine', 'maintance', 'improper', 'inadequate', 'error', 'lack', 'overran', 'weight', 'overloaded']
    key_takeoff = ['weather', 'fog', 'rain', 'stalled', 'engine', 'maintance', 'improper', 'inadequate', 'error', 'lack', 'overran', 'weight', 'overloaded']
    land_take_value = [(41, 43), (36, 20), (22, 23), (15, 52), (59, 230), (16, 28), (35, 38), (18, 28), (21, 17), (25, 2), (18, 25), (3, 16), (4, 35)]
    
    line_chart = pygal.HorizontalBar()
    line_chart.title = 'landing takeoff'
    #add keyword in x labels
    line_chart.x_labels = ['overloaded', 'weight', 'overran', 'lack', 'error', 'inadequate', 'improper', 'maintance', 'engine', 'stalled', 'rain', 'fog', 'weather']
    #add color in chart 
    line_chart.add('Landing', [{'value':land_take_value[12][0], 'color':'#99CCFF'}, {'value':land_take_value[11][0], 'color':'#99CCFF'}, {'value':land_take_value[10][0], 'color':'#99CCFF'},\
        {'value':land_take_value[9][0], 'color':'#99CCFF'}, {'value':land_take_value[8][0], 'color':'#99CCFF'}, {'value':land_take_value[7][0], 'color':'#99CCFF'}, {'value':land_take_value[6][0], 'color':'#99CCFF'}, \
        {'value':land_take_value[5][0], 'color':'#99CCFF'}, {'value':land_take_value[4][0], 'color':'#99CCFF'}, {'value':land_take_value[3][0], 'color':'#99CCFF'}, \
        {'value':land_take_value[2][0], 'color':'#99CCFF'}, {'value':land_take_value[1][0], 'color':'#99CCFF'}, {'value':land_take_value[0][0], 'color':'#99CCFF'} ])
    #add color in chart
    line_chart.add('Takeoff',  [{'value':land_take_value[12][1], 'color':'#FF99FF'}, {'value':land_take_value[11][1], 'color':'#FF99FF'}, {'value':land_take_value[10][1], 'color':'#FF99FF'},\
        {'value':land_take_value[9][1], 'color':'#FF99FF'}, {'value':land_take_value[8][1], 'color':'#FF99FF'}, {'value':land_take_value[7][1], 'color':'#FF99FF'}, \
        {'value':land_take_value[6][1], 'color':'#FF99FF'}, {'value':land_take_value[5][1], 'color':'#FF99FF'}, {'value':land_take_value[4][1], 'color':'#FF99FF'}, \
        {'value':land_take_value[3][1], 'color':'#FF99FF'}, {'value':land_take_value[2][1], 'color':'#FF99FF'}, {'value':land_take_value[1][1], 'color':'#FF99FF'}, {'value':land_take_value[0][1], 'color':'#FF99FF'}])
    line_chart.render_to_file('Landing Takeoff.svg')
count_land_take(df)
