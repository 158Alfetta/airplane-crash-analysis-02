"""Engine mechanism"""
import pandas as pd
def mechanism_problem():
    """about engine incluing malfunction, engine failed, technical problem, system, mechanical
fuel starvation, run out of fuel, ran out of fuel"""
    keyword_engine = ['malfunction', 'engine', 'technical problem', 'system', 'mechanical']
    keyword_fuel = ['fuel starvation', 'run out of fuel', 'ran out of fuel']
    keyword_body = ['fatigue fracture', 'airframe', 'fatigue failure', 'crack', \
    'empannage', 'fuselage', 'starboard', 'flap', 'slat', 'aileron', 'empennage', 'spoiler']
    df = pd.read_csv('C:\\Users\\Test\\Desktop\\airplane-crash-analysis\\dataset_psit.csv', encoding = "ISO-8859-1")
    summary = df.Summary.tolist()
    count_dic = {'Engine problem': 0, 'Fuel starvation': 0, 'Airframe problem': 0}
    for text in summary:
        text = str(text).lower()
        text_list = text.split()
        if any(key_eng in text for key_eng in keyword_engine):
            count_dic['Engine problem'] += 1
        elif any(key_body in text for key_body in keyword_body):
            count_dic['Airframe problem'] += 1
        if any(key_fuel in text for key_fuel in keyword_fuel):
            count_dic['Fuel starvation'] += 1
        for each in text_list:
            if each in ['wheel', 'wing', 'wings']:
                count_dic['Airframe problem'] += 1
    all_mechanism_problem = count_dic['Engine problem']+count_dic['Airframe problem']+count_dic['Fuel starvation']
    print(count_dic, {'All-Mechanism problem': all_mechanism_problem})
    return count_dic, {'All-Mechanism problem': all_mechanism_problem}
mechanism_problem()
