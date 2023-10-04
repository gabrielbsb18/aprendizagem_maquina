# Importação das bibliotecas necessárias
import os
import pandas as pd

# Obtém o caminho absoluto do diretório atual do arquivo
caminho_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho do arquivo CSV
caminho_arquivo_csv = os.path.join(caminho_atual, 'dados4.csv')

# Lê o arquivo CSV em um DataFrame
df = pd.read_csv(caminho_arquivo_csv)

# Calcula a contagem de homens e mulheres
gender_counts = df['sex'].value_counts()

# Exibe a contagem de homens e mulheres
print('Total de homens (male):', gender_counts['male'])
print('Total de mulheres (female):', gender_counts['female'])

