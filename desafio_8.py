##Relação entre idade e Modalidade##
##Gráfico de dispersão##

import matplotlib.pyplot as plt

df_plot = df_prouni_2020.copy()

df_plot['DATA_NASCIMENTO'] = pd.to_datetime(
    df_plot['DATA_NASCIMENTO'],
    dayfirst=True,
    errors='coerce'
)

df_plot['IDADE'] = 2020 - df_plot['DATA_NASCIMENTO'].dt.year

df_plot['MOD_NUM'] = (
    df_plot['MODALIDADE_ENSINO_BOLSA']
    .map({
        'EAD': 0,
        'PRESENCIAL': 1
    })
)

plt.figure(figsize=(8,5))

plt.scatter(
    df_plot['IDADE'],
    df_plot['MOD_NUM'],
    alpha=0.3
)

plt.title('Idade x Modalidade de Ensino')
plt.xlabel('Idade')
plt.ylabel('Modalidade')

plt.yticks(
    [0,1],
    ['EAD', 'Presencial']
)

plt.show()