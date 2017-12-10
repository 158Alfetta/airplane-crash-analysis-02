import pygal
import pandas as pd
def main():
    """use pandas as pd
    find hijack by keyword (hijack, bomb, grenade)
    hij = hijack, at = attack, sui = suicide"""
    df = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding = "ISO-8859-1")
    df2 = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\Countries.csv', encoding='ISO-8859-1')
    df3 = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\us_state.csv', encoding='ISO-8859-1')
    summary = df.Summary.tolist()
    location = df.Location.tolist()
    lst_location = []
    for i in range(len(summary)):        #for any row in .csv (jsut only Summary)
        text_low = str(summary[i]).lower()
        location_txt = str(location[i]).lower()
        if 'shot' in text_low or 'terror' in text_low or 'hijack' in text_low or 'bomb' in text_low:
            lst_location.append(location_txt)
    country = df2.a1.tolist()
    us_state = df3.b1.tolist()
    country_fi = {}
    country_count = {'us':0, 'gb':0, 'ru':0}
    for i in country:
        i = i.split('\t')
        country_fi[i[0]] = i[1]
    for j in country_fi:
        for k in lst_location:
            if country_fi[j].lower() in str(k):
                if j not in country_count:
                    country_count[j] = 1
                    lst_location.remove(k)
                else:
                    country_count[j] += 1
                    lst_location.remove(k)
    for l in us_state:
        for k in lst_location:
            if str(l).lower() in k:
                country_count['us'] += 1
    for k in lst_location:
        if 'england' in k:
            country_count['gb'] += 1
        elif 'ussr' in k:
            country_count['ru'] += 1
        elif 'russian' in k:
            country_count['ru'] += 1
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Attack location of all accident'
    worldmap_chart.add('Number of attack:', country_count)
    worldmap_chart.render_to_file('maps.svg')
main()