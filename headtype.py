"""type of plane"""
import pandas as pd
def headtype():
    """plane Type"""
    count = 0
    types = {}
    head = pd.read_csv('C:\\Users\\DELL\\Desktop\\dataset_psit.csv')
    head_type = head.Type.tolist()
    result_type = dict([(i, head_type.count(i)) for i in set(head_type)])
    typesorted = sorted(result_type.items(), key=lambda x: x[1], reverse=True)
    for key, value in typesorted:
        if count == 10:
            break
        else:
            types[key] = value
            count += 1
    return types
headtype()
