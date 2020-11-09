import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#tab = pd.read_csv(".../tabela-total+.csv", index_col = 0)
tab = pd.read_csv(".../tabela90-20+.csv", index_col = 0)

cols = tab[['ReLonX', 'ReLatY', 'ReLenCM', 'ReWgtKG','ReYear']].values

clus = KMeans(n_clusters=4)       
treino = clus.fit(cols)

fig = plt.figure(figsize = (5,5))
plot_1 = fig.add_subplot(1,1,1)
plot_1.spines['top'].set_visible(False) 
plot_1.spines['right'].set_visible(False) 

label = list(treino.cluster_centers_[:,2]) #comprimento
label.sort()
plt.scatter(treino.cluster_centers_[:,0], treino.cluster_centers_[:,1], edgecolor = 'indigo', s = treino.cluster_centers_[:,2],
            c = 'none', marker = "o", alpha=0.9)
for item in label:
    plt.scatter([], [], alpha=0.9, s=item,
                label=str(round(item,1)), marker = "o", c = 'none', edgecolor = 'indigo')

label = list(treino.cluster_centers_[:,3]) #peso
label.sort()
plt.scatter(treino.cluster_centers_[:,0], treino.cluster_centers_[:,1], edgecolor = 'none',
            s = treino.cluster_centers_[:,3], c = 'steelblue', alpha=0.7)
for item in label:
    plt.scatter([], [], alpha=0.7, s=item,
                label=str(round(item,1)), c='steelblue')


label = list(treino.cluster_centers_[:,4]) #ano
i = 0
while i < len(label):
    plt.annotate(str(int(label[i])), xy=(treino.cluster_centers_[i,0], treino.cluster_centers_[i,1]),
                 fontsize=8, xytext=(treino.cluster_centers_[i,0]+0.05, treino.cluster_centers_[i,1]+0.05))
    i = i + 1

plt.legend(scatterpoints=1, loc = 2, framealpha = 1, facecolor = 'white',
           frameon=True, ncol = 8, labelspacing=1, title = 'comprimento (cm) - peso (kg)',fontsize = 9)
plt.xticks(list(map(lambda x : round(x,2), treino.cluster_centers_[:,0])), fontsize = 9, rotation = 45)
plt.yticks(list(map(lambda x : round(x,2), treino.cluster_centers_[:,1])), fontsize = 9)
plt.xlabel('Longitude °', fontsize = 15)
plt.ylabel('Latitude °', fontsize = 15, rotation = 90)
plt.grid(linestyle='--', alpha = 0.3)


plt.quiver(-64.4,42.2,1,0.8, width=0.01, scale=6, color = 'grey', alpha = 0.3)
plt.title('Centróide respectivo ao peso, comprimento e ano de captura do L.nasus')
plt.show()

