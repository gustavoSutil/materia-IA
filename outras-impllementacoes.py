import pandas as pd
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering as ac


# Carregue os dados do arquivo CSV
data = pd.read_csv('dados.csv')
# Retira a primeira coluna (nome da pessoa) para realizar o agrupamento
x = data.iloc[:, 1:]

# Crie o modelo usando K-Means e define parâmetros essenciais (número de grupos/clusters)
modelo_ia_1 = ac(n_clusters=3)
# Treina o modelo
modelo_ia_1.fit(x)
# Adicione rótulos aos dados para indicar a qual grupo cada pessoa pertence
data['Grupo Agglomerative Clustering'] = modelo_ia_1.labels_
# Ordena dados usando coluna de agrupamento
data = data.sort_values(by=['Grupo Agglomerative Clustering'])
# Salva os resultados em arquivo
data.to_csv('resultado.csv', index=False)
print(data)

# Crie um DataFrame com os centros dos grupos
centros = pd.DataFrame(modelo_ia_1.cluster_centers_, columns=data.columns.values[1:-2])
# Arredonda valores com 2 casas decimais
centros = centros.round(2)
# Adicione uma coluna para identificar os centros dos grupos
centros['Agglomerative clustering'] = ['Centro ' + str(i) for i in range(modelo_ia_1.n_clusters)]
# Salva os resultados em arquivo
centros.to_csv('grupos.csv', index=False)
print(centros)