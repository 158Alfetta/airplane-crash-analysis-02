import pandas

def plane_type():

    #Change this to current csv directory.
    directory = 'C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv'
    counter = ''
    headercounter = 0
    priv_or_milt_counter = 0
    cargocounter = 0
    helicounter = 0
    returnlist = [0, 0, 0]
    maintext = pandas.read_csv(directory, encoding = "ISO-8859-1", header = None)
    for headercounter in maintext.index:
        maintextinloop = pandas.read_csv(directory, encoding = "ISO-8859-1", header = headercounter, usecols=[4])
        for counter in maintextinloop:
            counter = counter.lower()
            if ('private' in counter) | ('military' in counter):
                priv_or_milt_counter+=1
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
    passengerplane = maintext.shape[0]-(priv_or_milt_counter+cargocounter+helicounter)
    returndict = {}
    returndict["'private' and 'military' frequency"] = priv_or_milt_counter
    returndict["'cargo' frequency"] = cargocounter
    returndict["'helicopter' frequency"] = helicounter
    returndict["Number of passenger plane(s)"] = cargocounter
    print (returndict)
    return (returndict)

plane_type()
