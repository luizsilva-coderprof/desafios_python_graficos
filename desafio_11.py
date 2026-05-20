##Qual a proporção entre homens e mulheres beneficiários do Prouni em 2020?##
##Gráfico de Pizza##

import matplotlib.pyplot as plt

sexo = df_prouni_2020['SEXO_BENEFICIARIO'].value_counts()

plt.figure(figsize=(7,7))

plt.pie(
    sexo,
    labels=['Feminino', 'Masculino'],
    colors=['pink', 'lightblue'],
    autopct= lambda p: f'{p:.1f}%'
)
plt.title('Distribuição de beneficiários por sexo - 2020')

plt.show()