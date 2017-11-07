import pandas

def accident_freq():

    #Change this to current csv directory.
    directory = 'C:\\Users\\Lert Krush\\Desktop\\dataset_psit.csv'
    
    counter = ''
    headercounter = 0
    landingcounter = 0
    takeoffcounter = 0
    returnlist = [0, 0, 0]
    maintext = pandas.read_csv(directory, encoding = "ISO-8859-1", header = None)
    for headercounter in maintext.index:
        maintextinloop = pandas.read_csv(directory, encoding = "ISO-8859-1", header = headercounter)
        for counter in maintextinloop:
            counter = counter.lower()
            if 'landing' in counter:
                landingcounter+=1
                break
            if ('takeoff' in counter) | ('take off' in counter):
                takeoffcounter+=1
                break
    onflight = maintext.shape[0]-(landingcounter+takeoffcounter)
    returndict = {}
    returndict["'landing' frequency"] = landingcounter
    returndict["'takeoff' frequency"] = takeoffcounter
    returndict["Number of plane on flight(s)"] = onflight
    #print (returndict)
    return (returndict)

#accident_freq()
