# Importação das bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo CSV
df = pd.read_csv('dados4.csv')

# Criação do gráfico de dispersão
plt.scatter(df['age'], df['fare'], alpha=0.5)  # Criação do gráfico de dispersão
plt.xlabel('Idade')  # Rótulo do eixo x
plt.ylabel('Tarifa')  # Rótulo do eixo y
plt.title('Gráfico de Dispersão: Idade pela Tarifa')  # Título do gráfico
plt.show()  # Exibe o gráfico de dispersão

