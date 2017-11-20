import pandas as pd
import pygal
import operator
def ground():
    df = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding = "ISO-8859-1")
    date = df.Date.tolist()
    years = []
    dic_level = {}
    dic_data = {}
    dic_sort = {}
    list_lable = []
    list_val = []
    list_find = []
    for item in date:
        temp = item.split()
        years.append(temp[2])
    ground = df.Ground.fillna(0).tolist()
    flight = df.Flight.fillna('unknown').tolist()
    summary = df.Summary.tolist()
    level = df.level.tolist()
    for j in range(len(flight)):
        if flight[j] == '?':
            flight[j] = 'Unknown'
    for i in range(len(level)): #add level to dict()
        if int(ground[i]) > 5:
            dic_level[level[i]] = [years[i], flight[i], summary[i]]
    for i in range(len(ground)): # add ground people to compare
        if int(ground[i]) > 5:
            dic_data[level[i]] = ground[i]
    for j in sorted(dic_data.items(), key=operator.itemgetter(1), reverse=True):
        print
        list_val.append(j[1])
        list_in_text = dic_level[j[0]]
        list_find.append(list_in_text[2])
    print(list_find)
ground()