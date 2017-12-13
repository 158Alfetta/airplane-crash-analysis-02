import pandas as pd
import pygal
import operator
def ground():
    df = pd.read_csv('C:\\Users\\Asus\\Documents\\GitHub\\airplane-crash-analysis-02\\dataset_psit.csv', encoding = "ISO-8859-1")
    date = df.Date.tolist()
    years = []
    dic_level = {}
    dic_data = {}
    dic_sort = {}
    list_lable = []
    list_val = []
    list_find = []
    c_hi, c_sui, c_sho, c_take, c_oth = 0, 0, 0, 0, 0
    lst_co = []
    for item in date:
        temp = item.split()
        years.append(temp[2])
    ground = df.Ground.fillna(0).tolist()
    flight = df.Flight.fillna('unknown').tolist()
    summary = df.Summary.tolist()
    level = df.level.tolist()
    for j in range(len(flight)):
        if flight[j] == '?':
            flight[j] = 'Unknown'
    for i in range(len(level)): #add level to dict()
        if int(ground[i]) > 5:
            dic_level[level[i]] = [years[i], flight[i], summary[i]]
    for i in range(len(ground)): # add ground people to compare
        if int(ground[i]) > 5:
            dic_data[level[i]] = ground[i]
    for j in sorted(dic_data.items(), key=operator.itemgetter(1), reverse=True):
        print
        list_val.append(j[1])
        list_in_text = dic_level[j[0]]
        list_find.append(list_in_text[2])
    #วน for เพื่อเช็คkeyword ถ้ามีให้เก็บเข้าอีกตัวแปรของคำนั้นๆ
    for k in list_find:
        if "hijack" in k:
            c_hi += 1
            
        elif "suicide" in k:
            c_sui += 1
            
        elif "shot down" in k:
            c_sho += 1

        elif "takeoff" in k or "landing" in k or "take off" in k:
            c_take += 1
        else:
            c_oth += 1

    lst_co.append(c_hi)
    lst_co.append(c_sui)
    lst_co.append(c_sho)
    lst_co.append(c_take)
    lst_co.append(c_oth)
    lst_co.sort(reverse=True)


    line_chart = pygal.Bar()
<<<<<<< HEAD
    line_chart.title = 'Ground people accident use keyword'
    line_chart.x_labels = ['others', 'takeoff', 'hijack', 'suicide', 'shot down'] #add keyword in x labels
    #add color in chart
    line_chart.add('Ground people accident use keyword', [{'value':lst_co[0], 'color':'#6699FF'}, {'value':lst_co[1], 'color':'#CC99FF'}, {'value':lst_co[2], 'color':'#FF99FF'}, {'value':lst_co[3], 'color':'red'}, {'value':lst_co[4], 'color':'orange'}])
=======
    line_chart.title = 'Amount of ground people dead'
    line_chart.x_labels = ['others', 'attempt to takeoff/laning', 'hijack', 'suicide', 'shot down']
    line_chart.add('Amount of dead people on ground', [{'value':lst_co[0], 'color':'#6699FF'}, {'value':lst_co[1], 'color':'#CC99FF'}, {'value':lst_co[2], 'color':'#FF99FF'}, {'value':lst_co[3], 'color':'red'}, {'value':lst_co[4], 'color':'orange'}])
>>>>>>> f66628688cf98c18dd2833e7a90362a2f27a5e3d
    line_chart.render_to_file('ground_yaimai.svg')
ground()