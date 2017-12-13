import pandas
import pygal
def accident_freq():
    """to seperate of landing and takeoff"""
    directory = 'C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv'
    counter = ''
    list_label = []
    list_value = []
    headercounter = 0
    landingcounter = 0
    takeoffcounter = 0
    returnlist = [0, 0, 0]
    maintext = pandas.read_csv(directory, encoding = "ISO-8859-1", header = None)
    for headercounter in maintext.index:
        maintextinloop = pandas.read_csv(directory, encoding = "ISO-8859-1", header = headercounter)
        for counter in maintextinloop:  #word search and added to list 
            counter = counter.lower()
            if 'landing' in counter:
                landingcounter+=1
                break
            if ('takeoff' in counter) | ('take off' in counter):
                takeoffcounter+=1
                break
    onflight = maintext.shape[0]-(landingcounter+takeoffcounter)
    returndict = {}
    returndict['Landing'] = landingcounter
    returndict['Take off'] = takeoffcounter
    returndict['Number of plane on flight(s)'] = onflight
    line_chart = pygal.Bar()
    line_chart.title = 'Chart comparation with "Take off", "Landing", "On flight"'
    line_chart.x_labels = ['Landing', 'Take off', 'On flight(s)']
    line_chart.add('Frequency :', [landingcounter, takeoffcounter, onflight])
    line_chart.render_to_file('Status Bar.svg')
accident_freq()
