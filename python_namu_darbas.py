import requests as req
import bs4
import pandas as pand

darboPozicija = []
imone = []
alga = []
skelbiamosAlgosTipas = []

for puslapis in range(1, 72):
    nuoroda = "https://www.cvbankas.lt/?location=606&page={}".format(puslapis)
    url = req.get(nuoroda)
    html = bs4.BeautifulSoup(url.text, "lxml")

    a = html.find_all("a", {"class":"list_a can_visited list_a_has_logo"})

    for i in a:
        darboPozicija.append(i.find("h3", {"class":"list_h3"}).text)

        imone.append(i.find("span", {"class":"dib mt5"}).text)

        if(i.find("span", {"class":"salary_amount"}) != None):
            alga.append(i.find("span", {"class":"salary_amount"}).text)

        else:
            alga.append("Nenurodyta alga")

        if(i.find("span", {"class":"salary_calculation"}) != None):
            skelbiamosAlgosTipas.append(i.find("span", {"class":"salary_calculation"}).text)

        else:
            skelbiamosAlgosTipas.append("Nenurodytas algos tipas")
    
darbai = pand.DataFrame(zip(darboPozicija, imone, alga, skelbiamosAlgosTipas), columns = ["Darbo pozicija", "Įmonė", "Alga", "Skelbiamos algos tipas"])

darbai.to_excel('duomenys.xlsx', index = False)
