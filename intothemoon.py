"""fatality"""
import pandas as pd
import pygal
def main():
    """plane"""
    alla = []
    head = pd.read_csv('C:\\Users\\DELL\\Desktop\\dataset_psit.csv', encoding='ISO-8859-1')
    fatal = head.Fatalities.tolist()
    aboard = head.Aboard.tolist()
    for i in range(len(fatal)):
        alla.append(aboard[i]-fatal[i])
    list0 = 0
    list1 = 0
    list21 = 0#all omg inside here
    list41 = 0
    list61 = 0
    list80 = 0
    for i in range(len(alla)):
        if alla[i] == 0:
            list0 += 1
        elif alla[i] > 0:
            omg = ((alla[i]/aboard[i])*100)
            if omg > 0 and omg <= 20:
                list1 += 1
                omg = 0
            elif omg > 20 and omg <= 40:
                list21 += 1
                omg = 0
            elif omg > 40 and omg <= 60:
                list41 += 1
                omg = 0
            elif omg > 60 and omg <= 80:
                list61 += 1
                omg = 0
            elif omg > 80:
                list80 += 1
                omg = 0
    line_chart = pygal.HorizontalBar()
    line_chart.title = 'fatality in(%)'
    line_chart.add('0%', list0)
    line_chart.add('1%-20%', list1)
    line_chart.add('21%-40%', list21)
    line_chart.add('41%-60%', list41)
    line_chart.add('61%-80%', list61)
    line_chart.add('>80%', list80)
    line_chart.render('fatality.svg')
main()
