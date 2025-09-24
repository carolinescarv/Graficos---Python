import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('/Users/carolinecarvalho/Documents/EBAC/analista_de_dados/modulo 22/visualizacao_dados/ecommerce_estatistica.csv')

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200 )
print(df.head())
print(list(df.columns))

#GRAFICO DE HISTOGRAMA
plt.figure(figsize=(10,8))
plt.hist(df['Nota'], bins=10, color='pink', alpha=1)
plt.title('Distribuicao de Notas')
plt.xlabel('Nota')
plt.ylabel('Frequencia')
plt.show()

#GRAFICO DE DISPERSAO
plt.figure(figsize=(10,8))
plt.scatter(df['Preço'], df['N_Avaliações'])
plt.title('Relacao entre Preco e Numero de Avaliacoes')
plt.xlabel('Preco')
plt.ylabel('Numero de Avaliacoes')
plt.show()

#MAPA DE CALOR
df_corr=df[['Qtd_Vendidos_Cod', 'Nota', 'N_Avaliações_MinMax', 'Desconto', 'Preço', 'Marca_Freq', 'Material_Freq']].corr()

plt.figure(figsize=(10,8))
sns.heatmap(df_corr, annot=True, fmt='.2f')
plt.title('Mapa de Calor - relacao entre variaveis')
plt.xticks(rotation=30)
plt.show()

#GRAFICO DE BARRA
plt.figure(figsize=(10,8))
sns.countplot(x='Temporada', data=df, palette='pastel')
plt.title('Quantidade de Produtos por Temporada')
plt.xlabel('Temporada')
plt.ylabel('Quantidade de Produtos')
plt.xticks(rotation=30) 
plt.show()

#GRAFICO DE PIZZA
x = df['Gênero'].value_counts().index
y = df['Gênero'].value_counts().values
plt.figure(figsize=(10,8))
plt.pie(y, startangle=90)
plt.title('Distribuicao de Gênero')
plt.legend(x, title='Genero', loc='upper left', bbox_to_anchor=(1.05, 0.5))
plt.show()

#GRAFICO DE DENSIDADE
plt.figure(figsize=(10, 8))
sns.kdeplot(df['Preço'], fill=True, color="#395F16")
plt.title('Densidade de Precos')
plt.xlabel('Preco')
plt.show()

#GRAFICO DE REGRESSAO
plt.figure(figsize=(10,8))
sns.regplot(x='Qtd_Vendidos_Cod', y='Nota', data=df, color="#A581FA", scatter_kws={'color':"#DBCE0D"})
plt.title('Regressao Frequencia de Nota por Quantidade de Vendidos')
plt.xlabel('Quantidade de Vendidos')
plt.ylabel('Nota')
plt.show()