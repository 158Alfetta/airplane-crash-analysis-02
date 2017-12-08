def HijStat_AttStat_SuiStat():
    """use pandas as pd
    find hijack by keyword (hijack, bomb, grenade)
    hij = hijack, at = attack, sui = suicide"""
    keywords_hij = ['hijack', 'grenade']
    specific_bomb = ['bomb', 'bomber', 'bombing']
    keyword_att = 'shot'
    count_lst = []
    count_location = []
    df = pd.read_csv('/Users/punmanat/Documents/GitHub/airplane-crash-analysis-02/dataset_psit.csv', encoding = "ISO-8859-1")
    summary = df.Summary.tolist()
    location = df.Location.tolist()
    for i in range(len(summary)):        #for any row in .csv (jsut only Summary)
        text_low = str(summary[i]).lower()
        if keyword_att in text_low:
            count_lst.append(summary[i])
            count_location.append(location[i])
        elif keyword_hij in text_low:
            count_lst.append(summary[i])
            count_location.append(location[i])
    df = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\Countries.csv', encoding='ISO-8859-1')
    df3 = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\us_state.csv', encoding='ISO-8859-1')
    country = df.a1.tolist()
    us_state = df3.b1.tolist()
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
    print(country_count)
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Airplane Crashes Rate from 1970 - 2016 By Location'
    worldmap_chart.add('Crash Rate:', country_count)
    worldmap_chart.render_to_file('maps.svg')
main()