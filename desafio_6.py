##Qual raça/cor recebeu mais bolsas em 2020?##
##Gráfico de barras##

import matplotlib.pyplot as plt

racas = df_prouni_2020['RACA_BENEFICIARIO'].value_counts()

plt.figure(figsize=(8,5))
racas.plot(kind='bar')

plt.title('Bolsas por raça/cor - 2020')
plt.xlabel('Raça')
plt.ylabel('Quantidade')

plt.xticks(rotation=45)
plt.show()