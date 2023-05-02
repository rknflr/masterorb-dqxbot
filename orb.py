import pandas as pd
import string
import discord
import others

df = pd.read_excel('Master Orb.xlsx')
#print(df.head())

df['English'] = df['English'].apply(others.lower)
df['Vocation'] = df['Vocation'].apply(others.lower)

def orb_result(buscar):
    buscar = buscar.casefold()
    if(buscar.isdigit() or buscar == 'null'):
        return others.digitembed()

    elif(len(buscar) > 30):
        return others.longembed()
    else:
        find = df.loc[(df['English'] == buscar) | (df['Japanese'] == buscar)]
        find['English'] = find['English'].apply(others.upper)

        if(find.empty):
            results = df[df['English'].str.contains(buscar)]
            resultsRM = df[df['Romanized'].str.contains(buscar)]
            resultsVo = df[df['Vocation'].str.contains(buscar)]
            resultsJP = df[df['Japanese'].str.contains(buscar)]
            if(results.empty and resultsRM.empty and resultsJP.empty and resultsVo.empty):
                return others.emptyembed(buscar)
            else:
                count = 0
                merge1 = pd.merge(left=results,right=resultsRM,how="outer")
                merge2 = pd.merge(left=resultsVo,right=resultsJP,how="outer")
                mergeresult = pd.merge(left=merge1,right=merge2,how="outer")
                mergeresult['English'] = mergeresult['English'].apply(others.upper)
                return others.listedembed(mergeresult)
        else:
            return others.correctembed(find)


""" URL = "https://ethene.wiki/wiki/Master_Orb"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(class_="mw-parser-output")

titles = results.find_all(["h2","table"])

with open('orbs.csv','w',encoding="utf-8") as f:
    for i in titles:
        texto = i.find_all("td")
        row = ''
        for j in texto:
            if(j.text != ' '):
                row+= j.text+','

        if(row != ''):
            f.write(row[:-1])
            f.write('\n') """
        

