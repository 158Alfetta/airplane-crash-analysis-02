"""Find human_error stat
incluing 'pilot error', 'wrong', 'crew error, Improper maintenance"""
import pandas as pd
def human_error():
    """ will return 2 dict
        1.all of human error dict
        2.human error:'improper maintance and specific human error"""
    df = pd.read_csv('C:\\Users\\Test\\Desktop\\airplane-crash-analysis\\dataset_psit.csv', encoding = "ISO-8859-1")
    summary = df.Summary.tolist()
    keyword = ['pilot error', 'wrong', 'crew error']
    count_dic = {'Human error': 0, 'Improper maintenance': 0}
    for text in summary:
        text = str(text).lower()
        if any(key_hum in text for key_hum in keyword): #counting by use keyword check into text
            count_dic['Human error'] += 1
        elif 'maintenance' in text:
            count_dic['Improper maintenance'] += 1
    all_human_error = count_dic['Human error']+count_dic['Improper maintenance'] #find sum
    print(count_dic, {'All(Human error)': all_human_error})
    return count_dic, {'All(Human error)' : all_human_error}
human_error()
