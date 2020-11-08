import pandas as pd
import numpy as np

tab = pd.read_csv(".../tabela-total.csv", index_col = 0)
tab1 = pd.read_csv(".../tabela90-20.csv", index_col = 0)
tabs = [tab, tab1]
nome = ['tabela-total+','tabela90-20+']

cont = 0

for item in tabs:
    item = item[item['ReLenCM'].notna()]
    item = item[item['ReWgtKG'].notna()]
    item.index = list(range(0,len(item),1))
    item['Peso'] = np.where(item.ReWgtKG < 130, 0, 1) #peso adulto > 130
    item['Comprimento'] = np.where(item.ReLenCM < 170, 0, 1) #comprimento adulto > 170
    item['Ano'] = np.where(item.ReYear < 1996, 0, 1)
    item.to_csv(".../%s.csv" % nome[cont])
    cont = cont + 1
