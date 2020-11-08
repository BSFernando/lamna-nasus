import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

tab_total = pd.read_csv(".../tabela-total+.csv", index_col = 0)
tab_90_20 = pd.read_csv(".../tabela90-20+.csv", index_col = 0)

tabs = [tab_total, tab_90_20]
tit = ["1 curva", "2 curvas"]

n, p = stats.normaltest(tab_total['ReWgtKG'])
n1, p1 = stats.normaltest(tab_90_20['ReWgtKG'])
print('normaltest: tab_total / tab_90_20 (p-value)')
print(str(p) +" / "+ str(p1))

print('----------')

fig = plt.figure()
fig.subplots_adjust(hspace=0.5)
cont = 0
while cont < len(tabs):  
    fig.add_subplot(1,2,cont + 1)
    plt.hist(tabs[cont]['ReWgtKG'])
    plt.title(tit[cont])
    cont = cont + 1

plt.show() #distribuição não-normal

stat, p4 = stats.mannwhitneyu(tab_total['ReWgtKG'], tab_90_20['ReWgtKG'])
stat1, p5 = stats.wilcoxon(tab_total['ReWgtKG'], tab_90_20['ReWgtKG'])
print('mannwhitneyu / wilcoxon (p-value)')
print(str(p4) +" / "+ str(p5))
