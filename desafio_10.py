##Distribuição de idade por raça##
##Gráfico de caixa##

import matplotlib.pyplot as plt

dados = []

racas = df_prouni_2020['RACA_BENEFICIARIO'].dropna().unique()

for raca in racas:
    idade = df_prouni_2020[
        df_prouni_2020['RACA_BENEFICIARIO'] == raca
    ]['IDADE'].dropna()

    dados.append(idade)

plt.figure(figsize=(10,5))

plt.boxplot(dados, labels=racas)

plt.title('Idade por raça dos bolsistas')
plt.ylabel('Idade')

plt.xticks(rotation=45)

plt.show()