"""type of plane"""
import pandas as pd
def headtype():
    """plane Type"""
    count = 0
    types = {}
    head = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding='ISO-8859-1')
    head_type = head.Type.tolist()
    dicta = {}
    sorttype = sorted(types.items(), key=lambda x: x[1], reverse=True)
    lista = ['Lockheed C-130','Lockheed AC-130','Fokker F-27','Douglas C-47','Douglas DC-9','Beechcraft D 18S','Beechcraft 65','Ilyushin IL-62','Douglas DC-3','Hawker Siddeley']
    for i in range(155, 259):
        for j in lista:
            if j in head_type[i] and j in dicta:
                dicta[j] += 1
                break
            elif j in head_type[i] and j not in dicta:
                dicta[j] = 1
                break
    for i in dicta:
        print(i+' : '+str(dicta[i]))
headtype()
