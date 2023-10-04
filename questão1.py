# Importação da biblioteca pandas
import pandas as pd

# Leitura do arquivo CSV
df = pd.read_csv('dados4.csv')

# Ajuste das idades inválidas ou vazias para a moda
mode_age = df['age'].mode()[0]  # Calcula a moda das idades
df['age'].fillna(mode_age, inplace=True)  # Preenche idades inválidas com a moda

# Gravação do resultado no arquivo Resposta01.txt
df.to_csv('Resposta01.txt', index=False)  # Salva o DataFrame modificado em um novo arquivo CSV
