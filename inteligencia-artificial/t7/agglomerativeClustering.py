import pandas as pd
from sklearn.cluster import AgglomerativeClustering as ac
import numpy as np

#com isso voce calcula qual a distancia maxima sem crir um novo grupo
ACCEPTABLE_DISTANCE = 6
#defini 6 pois achei interresante

# Carregue os dados do arquivo CSV
data = pd.read_csv('dados.csv')
# Retira a primeira coluna (nome da pessoa) para realizar o agrupamento
x = data.iloc[:, 1:]

modelo_ia_1 = ac(n_clusters=None, distance_threshold=5)
# Treina o modelo
distance = modelo_ia_1.fit(x)
# Adicione rótulos aos dados para indicar a qual grupo cada pessoa pertence
data['Grupo Agglomerative Clustering'] = modelo_ia_1.labels_
data["distance"] = np.arange(len(modelo_ia_1.distances_)+1)
for i in range(len(modelo_ia_1.distances_-1)):
    data["distance"][i] = round(modelo_ia_1.distances_[i],2)
data["distance"][len(modelo_ia_1.distances_+1)] = round(-0,2)
# Ordena dados usando coluna de agrupamento
data = data.sort_values(by=['Grupo Agglomerative Clustering'])
# Salva os resultados em arquivo
data.to_csv('resultadoAC.csv', index=False)
print(data)

