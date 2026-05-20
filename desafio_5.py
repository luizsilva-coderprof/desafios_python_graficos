##Comparação de idade entre 2019 e 2020##
##Gráfico de Histograma##
import matplotlib.pyplot as plt

df_prouni_2019['DT_NASCIMENTO_BENEFICIARIO'] = pd.to_datetime(
    df_prouni_2019['DT_NASCIMENTO_BENEFICIARIO'],
    dayfirst=True,
    errors='coerce'
)

df_prouni_2019['IDADE'] = 2019 - df_prouni_2019['DT_NASCIMENTO_BENEFICIARIO'].dt.year

plt.figure(figsize=(10,5))

plt.hist(df_prouni_2019['IDADE'].dropna(),
         bins=20,
         alpha=0.5,
         label='2019',
         color='blue'
         )

plt.hist(df_prouni_2020['IDADE'].dropna(),
         bins=20,
         alpha=0.5,
         label='2020',
         color='red'
         )

plt.title('Distribuição de idade: 2019 x 2020')
plt.xlabel('Idade')
plt.ylabel('Quantidade')

plt.legend()
plt.show()