import pandas as pd
import pygal
from pygal.style import Style
def ground():
    df = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding = "ISO-8859-1")
    date = df.Date.tolist()
    years = []
    lst_all = []
    list_lable = []
    list_val = []
    for item in date:
        temp = item.split()
        years.append(temp[2])
    ground = df.Ground.tolist()
    flight = df.Flight.fillna('unknown').tolist()
    summary = df.Summary.tolist()
    for j in range(len(flight)):
        if flight[j] == '?':
            flight[j] = 'Unknown'
    for i in range(len(ground)):
        if int(ground[i]) >= 10:
            lst_all.append((int(ground[i]), years[i], flight[i], summary[i]))
    lst_all.sort(reverse=True)
    for k in lst_all:
        list_val.append(int(k[0]))
        list_lable.append('In '+str(k[1])+' On flight '+str(k[2])+' : '+str(k[3]))
    line_chart = pygal.Bar(show_x_labels=False)
    line_chart.title = 'Classification by cause that affect on accident'
    line_chart.x_labels = list_lable
    line_chart.add('Frequency :', list_val)
    line_chart.render_to_file('Ground People.svg')
ground()