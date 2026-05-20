####Qual estado (UF) teve mais bolsas em 2020?####
##Gráfico de barras##

import matplotlib.pyplot as plt

top_ufs = df_prouni_2020['UF_BENEFICIARIO'].value_counts().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
plt.barh(top_ufs.index, top_ufs.values)
#top_ufs.plot(kind='barh')

plt.title('Top 10 Estados com mais bolsas - 2020')
plt.xlabel('UF')
plt.ylabel('Quantidade de bolsas')
plt.xticks(rotation=0)
plt.yticks(rotation=0)

plt.show()