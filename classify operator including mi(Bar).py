"""type of operator"""
import pandas as pd
import pygal
def opertornoall():
    """operator"""
    count = 0
    operators = {}
    list_lable = []
    list_value = []
    ops = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding = "ISO-8859-1")
    ops_type = ops.Operator.tolist()
    ops_result = dict([(i, ops_type.count(i)) for i in set(ops_type)])
    opssorted = sorted(ops_result.items(), key=lambda x: x[1], reverse=True)
    for key, value in opssorted:
        if count == 10:
            break
        elif 'Military' in key or 'Private' in key or 'Air Taxi' in key:
            continue
        else:
            operators[value] = key
            count += 1
    for i in sorted(operators, reverse=True):
        list_lable.append(operators[i])
        list_value.append(i)
    line_chart = pygal.Bar()
    line_chart.title = 'Operator frequency rate top 10 since 1970 - 2016 (Including Military)'
    line_chart.x_labels = list_lable
    line_chart.add('Frequency :', list_value)
    line_chart.render_to_file('Operator frequency(mi).svg')
    """type of operator"""
    count = 0
    operators = {}
    list_lable = []
    list_value = []
    ops_type = ops.Operator.tolist()
    ops_result = dict([(i, ops_type.count(i)) for i in set(ops_type)])
    opssorted = sorted(ops_result.items(), key=lambda x: x[1], reverse=True)
    for key, value in opssorted:
        if count == 10:
            break
        elif 'Private' in key:
            continue
        elif 'Mili' in key:
            operators[value] = key
            count += 1
    for i in sorted(operators, reverse=True):
        list_lable.append(operators[i])
        list_value.append(i)
    line_chart = pygal.Bar()
    line_chart.title = 'Operator frequency rate top 10 since 1970 - 2016 (Without Military)'
    line_chart.x_labels = list_lable
    line_chart.add('Frequency :', list_value)
    line_chart.render_to_file('Operator frequency(non mi).svg')
opertornoall()
