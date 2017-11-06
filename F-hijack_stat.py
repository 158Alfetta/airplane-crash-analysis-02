"""find target 'ถูกปล้น'
HijackStat_AttackStat_SuicideStat"""
import pandas as pd
def HijStat_AttStat_SuiStat():
    """use pandas as pd
    find hijack by keyword (hijack, bomb, grenade)
    hij = hijack, at = attack, sui = suicide"""
    keywords_hij = ['hijack', 'grenade']
    specific_bomb = ['bomb', 'bomber', 'bombing']
    keyword_att = 'shot down'
    keyword_sui = 'suicide'
    count_dic = {'Hijack': 0, 'Attack': 0, 'Suicide': 0}
    df = pd.read_csv('C:\\Users\\Test\\Desktop\\airplane-crash-analysis\\dataset_psit.csv', encoding = "ISO-8859-1")
    summary = df.Summary.tolist()
    for text in summary:        #for any row in .csv (jsut only Summary)
        text_low = str(text).lower()
        if keyword_att in text_low:
            count_dic['Attack'] += 1
        if keyword_sui in text_low:
            count_dic['Suicide'] += 1
        text_list = str(text_low).split()      #make list() in list() cause need to check specific word
        for word in text_list:         #for word in text_list of list name 'summary'
            if word in specific_bomb:   # use for anti about another word 'bomb'does not relate such as 'bombay'
                count_dic['Hijack'] += 1
            elif any(key_hij in word for key_hij in keywords_hij):     #Let's check by keywords (each keyword)
                count_dic['Hijack'] += 1
    print(count_dic)
    return count_dic
HijStat_AttStat_SuiStat()
