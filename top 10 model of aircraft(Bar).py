"""type of plane"""
import pygal
import pandas as pd
import operator
def headtype():
    """plane Type"""
    count = 0
    types = {}
    type_all = {}
    head = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding='ISO-8859-1')
    head_type = head.Type.tolist()
    result_type = dict([(i, head_type.count(i)) for i in set(head_type)])
    typesorted = sorted(result_type.items(), key=lambda x: x[1], reverse=True)
    for key, value in typesorted:   #make new list types means top 20
        if count >= 20:
            type_all[key] = value
        else:
            types[key] = value
            count += 1
    for i in types: #print(list of type 20 for another check)
        print(i)
    return head_type    #use for anorther recheck
def recheck():
    """we found many bug about type so we need to recheck again by key that printed in first function
, So if we found some type same we will delete and set name for regular
de Havilland Canada DHC-6 Twin Otter
Douglas DC-3
Antonov AN-26
Yakovlev YAK-40
Cessna 208B
Embraer 110
McDonnell Douglas DC-9
Tupolev TU-134
Antonov AN-24
Antonov AN-12
CASA 212
Piper PA-31
Britten-Norman BN-2
Lockheed C-130
Fokker F-27
Piper PA-31
de Havilland DHC-2
"""
    list_type = headtype()
    list_lable = []
    list_val = []
    dict_of_type = {}
    count = 0
    list_plane = ['de Havilland Canada DHC-6 Twin Otter', 'Douglas DC-3', 'Antonov AN-26'\
, 'Yakovlev YAK-40', 'Cessna 208B', 'Embraer 110', 'McDonnell Douglas DC-9', 'Tupolev TU-134'\
, 'Antonov AN-24', 'Antonov AN-12', 'CASA 212', 'Piper PA-31', 'Britten-Norman BN-2', 'Lockheed C-130'
, 'Fokker F-27', 'Piper PA-31', 'de Havilland DHC-2']
    for i in list_plane:     #recheck about the same type in other key in dict() type_all
        for j in list_type:
            if i in str(j):
                if i not in dict_of_type:
                    dict_of_type[i] = 0
                else:
                    dict_of_type[i] += 1
    sorted_types = sorted(dict_of_type.items(), key=operator.itemgetter(1), reverse=True)
    types = dict(sorted_types)
    for i in types:
        if count < 10:
            list_lable.append(i)
            list_val.append(int(types[i]))
        else:
            break
        count += 1
    line_chart = pygal.Bar()
    line_chart.title = 'Top 10 model aircraft crashed since 1970 - 2016'
    line_chart.x_labels = list_lable
    line_chart.add('Frequency :', list_val)
    line_chart.render_to_file('Type_of_airplane.svg')
recheck()
