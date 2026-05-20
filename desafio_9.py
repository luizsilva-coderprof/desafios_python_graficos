##Qual modalidade de ensino cresceu de 2019 para 2020?##
##Gráfico de barras##
import matplotlib.pyplot as plt

modalidade_2019 = (
    df_prouni_2019['MODALIDADE_ENSINO_BOLSA']
    .value_counts()
)

modalidade_2020 = (
    df_prouni_2020['MODALIDADE_ENSINO_BOLSA']
    .value_counts()
)

comparacao = pd.DataFrame({
    '2019': modalidade_2019,
    '2020': modalidade_2020
}).fillna(0)

comparacao.plot(kind='bar', figsize=(8,5))

plt.title('Modalidade de ensino: 2019 x 2020')
plt.xlabel('Modalidade')
plt.ylabel('Quantidade')

plt.xticks(rotation=0)
plt.show()