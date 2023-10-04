# Importação das bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo CSV
df = pd.read_csv('dados4.csv')

# Calcular a porcentagem de sobreviventes e não sobreviventes
survived_counts = df['survived'].value_counts()

# Preparação para o gráfico de pizza
labels = ['Não Sobreviventes', 'Sobreviventes']
sizes = survived_counts.values
colors = ['lightcoral', 'lightskyblue']
explode = (0.1, 0)  # Explode a primeira fatia para destacar

# Criação do gráfico de pizza
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Para garantir que a pizza seja desenhada como um círculo.
plt.title('Porcentagem de Sobreviventes e Não Sobreviventes')
plt.show()  # Exibe o gráfico de pizza

