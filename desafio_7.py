##Bolsistas com deficiência Física##
##Gráfico de barras##

import matplotlib.pyplot as plt

deficiencia = df_prouni_2020[
    'BENEFICIARIO_DEFICIENTE_FISICO'
].value_counts()

plt.figure(figsize=(6,4))
# deficiencia.plot(kind='bar')
plt.bar(deficiencia.index, deficiencia.values)

plt.title('Beneficiários com deficiência física')
plt.xlabel('Possui deficiência?')
plt.ylabel('Quantidade')

plt.xticks(rotation=0)
plt.show()