import pandas as pd
def ground():
    df = pd.read_csv('C:\\Users\\Test\\Desktop\\airplane-crash-analysis\\clean_data_year.csv', encoding = "ISO-8859-1")
    date = df['Date']
    years = []
    diction = {}
    diction_sort = {}
    count = 0
    for item in date:
        temp = item.split()
        years.append(temp[2])
    ground = df.Ground.tolist()
    summary = df.Summary.tolist()
    flight = df.Flight.tolist()
    for i in range(len(ground)):
        if int(ground[i]) != 0:
            diction[int(ground[i])] = [years[i], flight[i], summary[i]]
    for j in sorted(diction, reverse=True):
        diction_sort[j] = diction[j]
        if count == 10:
            break
return diction_sort # just only top ten ground people
#return diction  # all data that ground != 0
ground()