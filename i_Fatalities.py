import pandas as pd
def Fatalities():
    """Top 10 plane crashes by passengers killed
    return dict len() = 10"""
    df = pd.read_csv('/Users/chutikarn/Documents/PsitPro/dataset_psit.csv', encoding='ISO-8859-1')
    fatal = df.Fatalities.tolist()
    flight = df.Flight.tolist()
    diction = {}
    diction_sort = {}
    for i in range(len(fatal)):
        diction[fatal[i]] = flight[i]
    for j in sorted(diction, reverse=True):
        diction_sort[j] = diction[j]
    print(diction_sort)
Fatalities()
