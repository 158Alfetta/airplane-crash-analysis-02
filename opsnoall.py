"""type of operator"""
import pandas as pd
def opertornoall():
    """operator"""
    count = 0
    operators = {}
    ops = pd.read_csv('C:\\Users\\DELL\\Desktop\\datasetpsit.csv')
    ops_type = ops.Operator.tolist()
    ops_result = dict([(i, ops_type.count(i)) for i in set(ops_type)])
    opssorted = sorted(ops_result.items(), key=lambda x: x[1], reverse=True)
    for key, value in opssorted:
        if count == 10:
            break
        elif 'Military' in key or 'Private' in key or 'Air Taxi' in key:
            continue
        else:
            operators[key] = value
            count += 1
    return operators
opertornoall()
