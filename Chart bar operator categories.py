import pandas
import pygal
def plane_type():

    #Change this to current csv directory.
    directory = 'C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv'
    counter = ''
    headercounter = 0
    priv = 0
    milt_counter = 0
    cargocounter = 0
    helicounter = 0
    returnlist = [0, 0, 0]
    maintext = pandas.read_csv(directory, encoding = "ISO-8859-1", header = None)
    for headercounter in maintext.index:
        maintextinloop = pandas.read_csv(directory, encoding = "ISO-8859-1", header = headercounter, usecols=[4])
        for counter in maintextinloop:
            counter = counter.lower()
            if ('private' in counter):
                priv += 1
                break
            elif  ('military' in counter):
                milt_counter+=1
                break
        maintextinloop = pandas.read_csv(directory, encoding = "ISO-8859-1", header = headercounter, usecols=[10])
        for counter in maintextinloop:
            counter = counter.lower()
            if ('cargo' in counter):
                cargocounter+=1
                break
        for counter in maintextinloop:
            counter = counter.lower()
            if ('helicopter' in counter):
                helicounter+=1
                break
    passengerplane = maintext.shape[0]-(milt_counter+cargocounter+helicounter+priv)
    line_chart = pygal.Bar()
    line_chart.title = 'Operator by categories'
    line_chart.x_labels = ["Passenger","Military", "Cargo", "Private"]
    line_chart.add('Frequency :', [passengerplane, milt_counter, cargocounter, priv])
    line_chart.render_to_file('Bar Operator categories.svg')
plane_type()
