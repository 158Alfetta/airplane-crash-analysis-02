def main():
    import xlsxwriter
    import urllib.request
    from bs4 import BeautifulSoup
    workbook = xlsxwriter.Workbook('2015.xlsx')
    worksheet = workbook.add_worksheet()
    for n in range(1, 22+1):
        print("Progress :", "%.2f" %((n/22)*100), '%')
        opener = urllib.request.FancyURLopener({})
        liss = []
        url = "http://www.planecrashinfo.com/2015/2015-"+str(n)+".htm"
        f = opener.open(url)
        soup = BeautifulSoup(f.read(), "lxml")
        text = soup.get_text()
        text_2 = text.splitlines()
        for i in text_2:
            text_3 = ""
            for j in i:
                if j.isalpha() == 1 or j.isdigit() == 1 or j in ["'", ' ', '.', ':', ',', '-', '?', '#']:
                    text_3 += j
            if len(text_3) > 0:
                liss.append(text_3)
        count = 0
        final = []
        for k in liss:
            count += 1 
            if k in ['Date:']:
                final.append(liss[liss.index(k)+1])
        col = 0
        for m in final:
            worksheet.write(n, col, m)
            col += 1
    
    workbook.close()
main()