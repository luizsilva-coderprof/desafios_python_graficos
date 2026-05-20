####Qual turno teve mais bolsas em 2020?####
##Gráfico de barras##

import matplotlib.pyplot as plt

turnos = df_prouni_2020['NOME_TURNO_CURSO_BOLSA'].value_counts()

plt.figure(figsize=(8,5))
plt.bar(turnos.index, turnos.values, color='red')
#turnos.plot(kind='bar')

plt.title('Bolsas por Turno - 2020')
plt.xlabel('Turno')
plt.ylabel('Quantidade')

plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()