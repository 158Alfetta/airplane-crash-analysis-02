"""type of plane"""
import pandas as pd
def headtype():
    """plane Type"""
    count = 0
    types = {}
    type_all = {}
    head = pd.read_csv('C:\\Users\\Test\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding='ISO-8859-1')
    head_type = head.Type.tolist()
    result_type = dict([(i, head_type.count(i)) for i in set(head_type)])
    typesorted = sorted(result_type.items(), key=lambda x: x[1], reverse=True)
    for key, value in typesorted:   #make new list types means top 10
        if count > 10:
            type_all[key] = value
        else:
            types[key] = value
            count += 1
    for key_2 in types:     #recheck about the same type in other key in dict() type_all
        for key_3 in type_all:
            if key_2 in str(key_3):
                types[key_2] += type_all[key_3]
    return types
headtype()
