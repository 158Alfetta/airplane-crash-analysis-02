import pygal
import pandas as pd
def Fatalities():
    """the function will get a year from 'Date'column on dataset and 'Fatalities' to make a dictionary every year
    ex. 2016: 553 | 553 is a sum of fatalities of year"""
    df = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding = "ISO-8859-1")
    fatal = df.Fatalities.fillna(0).tolist()
    year = df.Date.tolist()
    year_clean = []
    all_fatalities = 0
    diction = {}
    diction_sort = {}
    diction_year = {}
    diction_year_sort = {}
    for i in year:
        i_2 = i.split(" ")
        year_clean.append(i_2[2])
        if i_2[2] not in diction_year:
            diction_year[i_2[2]] = 1
        else:
            diction_year[i_2[2]] += 1 
    for i in range(len(fatal)):
        if year_clean[i] not in diction:
            diction[year_clean[i]] = int(fatal[i])
        else:
            diction[year_clean[i]] += int(fatal[i])
    for j in sorted(diction):
        diction_sort[j] = diction[j]
        all_fatalities += diction[j]
    for i in sorted(diction_year):
        diction_year_sort[i] = diction_year[i]
    #return [diction_sort, {'all_fatalities':all_fatalities}, diction_year]
    return [diction_sort, diction_year]
def chart():
    list_of_all = Fatalities()
    dict_fatal = list_of_all[0]
    dict_year = list_of_all[1]
    list_lable_fatal = []
    list_lable_year = []
    list_value_fatal = []
    list_value_year = []
    for i in dict_fatal:
        list_lable_fatal.append(i)
        list_value_fatal.append(dict_fatal[i])
    for j in dict_year:
        list_lable_year.append(j)
        list_value_year.append(dict_year[j])
    line_chart = pygal.Line(x_label_rotation=90, fill=True)
    line_chart.title = 'fatalities per years in 1970 - 2016'
    line_chart.x_labels = list_lable_fatal
    line_chart.add('Fatalities', list_value_fatal)
    line_chart2 = pygal.Line(x_label_rotation=90, fill=True)
    line_chart2.title = 'Line of airplane accident per year in 1970 - 2016'
    line_chart2.x_labels = list_lable_year
    line_chart2.add('Frequency', list_value_year)
    line_chart.render_to_file('fatal.svg')
    line_chart2.render_to_file('year.svg')
chart()
