import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Carregando dados
iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')

# Gráfico 1: Dispersão com Matplotlib
plt.figure(figsize=(10, 6))
colors = {'setosa': 'red', 'versicolor': 'blue', 'virginica': 'green'}

for species in iris['species'].unique():
    subset = iris[iris['species'] == species]
    plt.scatter(subset['sepal_length'], subset['sepal_width'], 
                c=colors[species], label=species, alpha=0.7)

plt.xlabel('Comprimento da Sépala (cm)')
plt.ylabel('Largura da Sépala (cm)')
plt.title('Relação entre Comprimento e Largura da Sépala por Espécie')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("matplot_dispersao.png")  # Salva o gráfico
plt.show()

# Gráfico 2: Boxplot com Matplotlib
plt.figure(figsize=(12, 6))
species_data = [iris[iris['species'] == sp]['petal_length'] for sp in iris['species'].unique()]
plt.boxplot(species_data, labels=iris['species'].unique())
plt.ylabel('Comprimento da Pétala (cm)')
plt.title('Distribuição do Comprimento da Pétala por Espécie')
plt.grid(True, alpha=0.3)
plt.savefig("matplot_boxplot.png")  # Salva o gráfico
plt.show()