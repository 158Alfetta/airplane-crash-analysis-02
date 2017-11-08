import pandas as pd
def allyear():
    df = pd.read_csv('dataset_psit.csv', encoding = "ISO-8859-1")
    date = df.Date
    years = []
    for i in date:
        temp = i.split()
        years.append(temp[2])
    new_year = {}
    for year in years:
        if year not in new_year:
            new_year[year] = 1
        else:
            new_year[year] += 1
    return new_year
allyear()
