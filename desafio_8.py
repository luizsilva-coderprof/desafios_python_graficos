##Relação entre idade e tipo de bolsa##
##Gráfico de dispersão##

import matplotlib.pyplot as plt

df_plot = df_prouni_2020.copy()

df_plot['TIPO_NUM'] = (
    df_plot['TIPO_BOLSA']
    .map({'PARCIAL': 0, 'INTEGRAL': 1})
)

plt.figure(figsize=(8,5))

plt.scatter(
    df_plot['IDADE'],
    df_plot['TIPO_NUM'],
    alpha=0.3
)

plt.title('Idade x Tipo de Bolsa')
plt.xlabel('Idade')
plt.ylabel('Tipo da bolsa')

plt.yticks([0,1], ['Parcial', 'Integral'])

plt.show()