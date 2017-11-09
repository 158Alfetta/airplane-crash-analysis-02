"""type of plane"""
import pygal
import pandas as pd
import operator
def headtype():
    """plane Type"""
    count = 0
    types = {}
    type_all = {}
    list_lable = []
    list_val = []
    head = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding='ISO-8859-1')
    head_type = head.Type.tolist()
    result_type = dict([(i, head_type.count(i)) for i in set(head_type)])
    typesorted = sorted(result_type.items(), key=lambda x: x[1], reverse=True)
    for key, value in typesorted:   #make new list types means top 10
        if count > 10:
            type_all[key] = value
        else:
            types[key] = value
            count += 1
    for key_2 in types:     #recheck about the same type in other key in dict() type_all
        for key_3 in type_all:
            if key_2 in str(key_3):
                types[key_2] += type_all[key_3]
    sorted_types = sorted(types.items(), key=operator.itemgetter(1))
    types = {}
    for j,k in sorted_types:
        types[j] = k
    for i in types:
        list_lable.append(i)
        list_val.append(int(types[i]))
    list_lable2 = list_lable[-1::-1]
    list_val2 = list_val[-1::-1]
    line_chart = pygal.Bar()
    line_chart.title = 'Top 10 of most airplane crashed since 1970 - 2016 '
    line_chart.x_labels = list_lable2
    line_chart.add('Frequency :', list_val2)
    line_chart.render_to_file('Type_of_airplane.svg')
headtype()
