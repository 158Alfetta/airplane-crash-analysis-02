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
    year = {1970: {}, 1971: {}, 1972: {}, 1973: {}, 1974: {}, 1975: {}, 1976: {}, 1977: {}, 1978: {}, 1979: {}, 1980: {}, 1981: {}, 1982: {}, 1983: {}, 1984: {}, 1985: {}, 1986: {}, 1987: {}, 1988: {}, 1989: {}, 1990: {}, 1991: {}, 1992: {}, 1993: {}, 1994: {}, 1995: {}, 1996: {}, 1997: {}, 1998: {}, 1999: {}, 2000: {}, 2001: {}, 2002: {}, 2003: {}, 2004: {}, 2005: {}, 2006: {}, 2007: {}, 2008: {}, 2009: {}, 2010: {}, 2011: {}, 2012: {}, 2013: {}, 2014: {}, 2015: {}, 2016: {}}
    years = []
    maintext = pd.read_csv(directory, encoding = "ISO-8859-1", header = None)
    for i in date:
        too = i.split()
        years.append(too[2])
    for i in years:
        if i in year:
            for headercounter in maintext.index:
                maintextinloop = pd.read_csv(directory, encoding = "ISO-8859-1", header = headercounter, usecols=[4])
                for counter in maintextinloop:
                    counter = counter.lower()
                    if 'private' in counter:
                        year[i][private] += 1
                        break
                    elif 'military' in counter:
                        year[i][military] += 1
                        break
                    elif 'express' in counter:
                        year[i][express] += 1
                        break
                    elif 'air' in counter:
                        year[i][airline] += 1
                        break
    print(year)
plane_type()
