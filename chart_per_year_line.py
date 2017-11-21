import pandas as pd
import pygal
def plane_type():
    #Change this to current csv directory.
    df = pd.read_csv('C:\\Users\\DELL\\Desktop\\dataset_psit.csv', encoding = "ISO-8859-1")
    date = df['Date']
    directory = 'C:\\Users\\DELL\\Desktop\\dataset_psit.csv'
    counter = ''
    headercounter = 0
    returnlist = [0, 0, 0]
    dict_year = {}
    year = {'1970': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1971': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1972': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1973': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1974': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1975': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1976': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1977': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1978': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1979': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1980': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1981': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1982': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1983': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1984': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1985': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1986': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1987': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1988': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1989': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1990': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1991': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1992': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1993': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1994': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1995': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1996': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1997': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1998': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '1999': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2000': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2001': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2002': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2003': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2004': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2005': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2006': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2007': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2008': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2009': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2010': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2011': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2012': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2013': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2014': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2015': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}, '2016': {'Pri': 0, 'Mil': 0, 'Car': 0, 'All': 0}}
    years = []
    counter = df.Summary.fillna('nothing').tolist()
    for i in date:
        too = i.split()
        years.append(too[2])
    count = 0
    countt = 0
    for i in range(len(counter)):
        param = years[i]
        count += 1
        if 'private' in counter[i]:
            year[param]['Pri'] += 1
            countt += 1
        elif 'military' in counter[i]:
            year[param]['Mil'] += 1
            countt += 1
        elif 'cargo' in counter[i]:
            year[param]['Car'] += 1
            countt += 1
        else:
            year[param]['All'] += 1
            countt += 1

    lista = []
    listb = []
    listc = []
    listd = []
    for i in year:
        lista.append(year[i]["Pri"])
        listb.append(year[i]["Mil"])
        listc.append(year[i]["Car"])
        listd.append(year[i]["All"])

    line_chart = pygal.Line()
    line_chart.title = 'most accident of plane type'
    line_chart.x_labels = year
    line_chart.add('private', lista)
    line_chart.add('military', listb)
    line_chart.add('air cargo', listc)
    line_chart.add('airline', listd)
    line_chart.render_to_file('most_summary_line.svg')
plane_type()
