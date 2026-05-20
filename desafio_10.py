##Distribuição de idade por raça##
##Gráfico de caixa##

import matplotlib.pyplot as plt

dados = []

df_prouni_2020['DATA_NASCIMENTO'] = pd.to_datetime(
    df_prouni_2020['DATA_NASCIMENTO'],
    dayfirst=True,
    errors='coerce'
)

df_prouni_2020['IDADE'] = 2020 - df_prouni_2020['DATA_NASCIMENTO'].dt.year

racas = df_prouni_2020['RACA_BENEFICIARIO'].dropna().unique()

for raca in racas:
    idade = df_prouni_2020[df_prouni_2020['RACA_BENEFICIARIO'] == raca]['IDADE'].dropna()
    dados.append(idade)


plt.figure(figsize=(10,5))
plt.boxplot(dados, tick_labels=racas)
plt.title('Idade por raça dos bolsistas')
plt.ylabel('Idade')
plt.xticks(rotation=45)
plt.show()