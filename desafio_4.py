##Idade dos beneficiários por sexo##
##Gráfico de Caixa##

import matplotlib.pyplot as plt

homens = df_prouni_2020[
    df_prouni_2020['SEXO_BENEFICIARIO'] == 'M'
]['IDADE']

mulheres = df_prouni_2020[
    df_prouni_2020['SEXO_BENEFICIARIO'] == 'F'
]['IDADE']

plt.figure(figsize=(8,5))

plt.boxplot([homens.dropna(), mulheres.dropna()],
            labels=['Homens', 'Mulheres'])

plt.title('Idade dos bolsistas por sexo - 2020')
plt.ylabel('Idade')

plt.show();