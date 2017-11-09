import pygal
import pandas as pd
def main():
    df = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\Countries.csv', encoding='ISO-8859-1')
    df2 = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding='ISO-8859-1')
    df3 = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\us_state.csv', encoding='ISO-8859-1')
    country = df.a1.tolist()
    us_state = df3.b1.tolist()
    location = df2.Location.tolist()
    country_fi = {}
    us_state_fi = {}
    country_count = {'us':0}
    for i in country:
        i = i.split('\t')
        country_fi[i[0]] = i[1]
    for j in country_fi:
        for k in location:
            if country_fi[j] in str(k):
                if j not in country_count:
                    country_count[j] = 1
                    location.remove(k)
                else:
                    country_count[j] += 1
                    location.remove(k)
    for l in us_state:
        for k in location:
            if str(l) in k:
                country_count['us'] += 1
    country_count['us'] = min(country_count['us'], 155)
    print(country_count)
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Airplane Crashes Rate from 1970 - 2016 By Location'
    worldmap_chart.add('Crash Rate:', country_count)
    worldmap_chart.render_to_file('maps.svg')
main()