import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

tabela = pd.read_csv(".../TAB.csv", index_col = 0)

tab = tabela[(tabela['ReLenCM'].notna()) & (tabela['ReWgtKG'].notna())]
tabela90 = tab[tab['ReYear']  < 1996]
tabela20 = tab[tab['ReYear']  > 1995]

tabelas = [tabela90, tabela20, tab]
titulo = ['tabela-90', 'tabela-20', 'tabela-total']

fig = plt.figure(figsize = (20, 15))
fig.subplots_adjust(hspace = 0.5)

cont = 1

for item in tabelas:
    
    tab_peso_comp = item.drop(columns=['ReYear', 'ReDate', 'ReLatY', 'ReLonX'])
    comprimento = tab_peso_comp['ReLenCM'].values
    peso = tab_peso_comp['ReWgtKG'].values

    def model(z, b, a):    #função Wt = a.(Lt^b)
        return a * (z ** b) 

    popt, pcov = curve_fit(model, comprimento, peso)

    x = np.arange(1,300,0.1)

    #fig = plt.figure()

    fig.add_subplot(2,2,cont)

    plt.scatter(comprimento, peso, s = 5, c = 'k')
    plt.plot(x, popt[1] * (x ** popt[0]), c = 'red')
    plt.xlabel("Comprimento CM")
    plt.ylabel("Peso KG")
    plt.xticks(fontsize = 8)
    plt.yticks(fontsize = 8)
    plt.title("%s" % titulo[cont-1])
    
    tab = pd.read_csv(".../TAB.csv", index_col = 0)
    tab = tab[tab['ReLenCM'].notna()]
    tab['ReWgtKG'] = tab['ReWgtKG'].fillna(popt[1] * (tab['ReLenCM']  ** popt[0]))
    tab.to_csv(".../%s.csv" % titulo[cont-1])
    
    cont = cont + 1

plt.show() # mostrando curvas peso_comp < 95 (fase negativa OMA), > 95 (fase positiva OMA) e todos os anos (fase +-)

tab = pd.read_csv(".../tabela-90.csv", index_col = 0)
tabela90 = tab[tab['ReYear']  < 1996]

tab1 = pd.read_csv(".../tabela-20.csv", index_col = 0)
tabela20 = tab1[tab1['ReYear']  > 1995]

tab_conc = pd.concat([tabela90, tabela20])
tab_conc.to_csv(".../tabela90-20.csv")

