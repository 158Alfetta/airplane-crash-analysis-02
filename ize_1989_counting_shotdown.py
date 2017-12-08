"""1989 counting shotdown"""
import pandas as pd
def shotdown():
    """counting shotdown"""
    keyword_att = 'shot'
    count1989 = 0
    count1988 = 0
    count1990 = 0
    df = pd.read_csv('C:\\Users\\Asus\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding = "ISO-8859-1")
    summary = df.Summary.tolist()
    for i in range(1457-1,1552+1):        #for any row in .csv (jsut only Summary)
        text_low = str(summary[i]).lower()
        if keyword_att in text_low:
            count1989 += 1
    for j in range(1379-1,1456+1):
        text_low = str(summary[j]).lower()
        if keyword_att in text_low:
            count1988 += 1
    for k in range(1548-1,1624+1):
        text_low = str(summary[k]).lower()
        if keyword_att in text_low:
            count1990 += 1
    print(count1988, count1989, count1990)
shotdown()
