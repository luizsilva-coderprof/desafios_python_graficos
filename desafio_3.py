##Distribuição de idade dos bolsistas em 2020##
##Gráfico de Histograma##

import pandas as pd
import matplotlib.pyplot as plt

df_prouni_2020['DATA_NASCIMENTO'] = pd.to_datetime(
    df_prouni_2020['DATA_NASCIMENTO'],
    dayfirst=True,
    errors='coerce'
)

df_prouni_2020['IDADE'] = 2020 - df_prouni_2020['DATA_NASCIMENTO'].dt.year

plt.figure(figsize=(10,5))
plt.hist(df_prouni_2020['IDADE'].dropna(), bins=20)

plt.title('Distribuição de idade dos bolsistas - 2020')
plt.xlabel('Idade')
plt.ylabel('Quantidade')
plt.xticks(
    range(
        int(df_prouni_2020['IDADE'].min()),
        int(df_prouni_2020['IDADE'].max()) + 1,
        5
    )
)

plt.show()