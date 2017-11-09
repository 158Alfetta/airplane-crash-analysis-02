import pandas as pd
def ground():
    df = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding = "ISO-8859-1")
    date = df.Date.tolist()
    years = []
    diction = {}
    diction_sort = {}
    for item in date:
        temp = item.split()
        years.append(temp[2])
    ground = df.Ground.tolist()
    flight = df.Flight.fillna('unknown').tolist()
    summary = df.Summary.tolist()
    for j in range(len(flight)):
        if flight[j] == '?':
            flight[j] = 'Unknown'
    for i in range(len(ground)):
        if int(ground[i]) != 0:
            diction[int(ground[i])] = [years[i], flight[i], summary[i]]
    for j in sorted(diction, reverse=True):
        diction_sort[j] = diction[j]
    print(diction_sort)
    return diction_sort # just only top ten ground people
    #return diction  # all data that ground != 0
ground()