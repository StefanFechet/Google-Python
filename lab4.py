from selenium import webdriver
import pandas as pd
import matplotlib.pyplot as plt

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
dictionar = {'Judet': []}
start = 3
stop = 27
for k in range(start, stop):
    try:
        browser.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-' + str(k) + '-aprilie-2020-ora-13-00/')
        table = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/main/article/div/div/table[1]')
        tabel = table.text
        lista = tabel.split("\n")
        lista.pop()
        dictionar[str(k) + ' aprilie 2020'] = []
        for j in range(0, 2):
            for i in range(j, len(lista)):
                x = lista[i]
                row = x.split()
                if k == start:
                    if j % 2 == 0:
                        dictionar['Judet'].append(row[-2])
                if j % 2 == 1 and len(dictionar[str(k) + ' aprilie 2020']) < 42:
                    dictionar[str(k) + ' aprilie 2020'].append(row[-1])
    except:
        continue
browser.close()

dictionar['Judet'].remove('cazuri')
df = pd.DataFrame(dictionar)
df.to_excel('covid.xls')
wb = pd.read_excel('covid.xls')
wb.to_html('pandemie.html')

l = []
days = []

judet = input("Introduceti numele unui judet: ")
try:
    plt.title(judet)
    poz = dictionar['Judet'].index(judet)
    for k in dictionar.keys():
        if k != 'Judet':
            l.append(dictionar[k][poz])
            days.append(k.split(' ')[0])
    plt.plot(days, l)
    plt.show()
except:
    print("Nu exista acest judet")
