"""fatality"""
import pandas as pd
import pygal
def main():
    """plane"""
    alla = []
    head = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding='ISO-8859-1')
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
    for i in range(len(aboard)):
        if alla[i] == 0:
            list0 += 1
            continue
        elif alla[i] > 0:
            omg = ((alla[i]/aboard[i])*100)
            if omg >= 1 and omg <= 20:
                list1 += 1
                omg = 0
            elif omg >= 21 and omg <= 40:
                list21 += 1
                omg = 0
            elif omg >= 41 and omg <= 60:
                list41 += 1
                omg = 0
            elif omg >= 61 and omg <= 80:
                list61 += 1
                omg = 0
            elif omg > 80:
                list80 += 1
                omg = 0
    print(list1, list21, list41, list61, list80)
    pie_chart = pygal.Bar()
    pie_chart.title = 'fatality'
    pie_chart.add('0%', list0)
    pie_chart.add('1\\%-20\\%', list1)
    pie_chart.add('21\\%-40\\%', list21)
    pie_chart.add('41\\%-60\\%', list41)
    pie_chart.add('61\\%-80\\%', list61)
    pie_chart.add('>80%', list80)
    pie_chart.render('fatality.svg')
main()
