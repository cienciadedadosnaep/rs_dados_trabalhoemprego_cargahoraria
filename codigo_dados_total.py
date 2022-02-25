import pandas as pd

df = pd.read_csv('E:/Área de trabalho/Códigos/R/rs_dados_trabalhoemprego_cargahoraria/data/TAB_6406_populacao_ocupada_SIDRA_PNAD_CTRIMESTRAL.csv')
#df.info()
selecao = 'Média de horas habitualmente trabalhadas por semana no trabalho principal das pessoas de 14 anos ou mais de idade'
grafico = df[["Trimestre","Valor","Variável","Cor ou raça"]]
grafico1 = grafico[grafico['Variável']==selecao]
grafico1 = grafico1[grafico['Cor ou raça']=='Total']
#grafico1.info() 
#print(grafico1.head(5))
graf1 = grafico1[['Trimestre','Valor']].reset_index(drop=True)
#print(graf1.tail(10))
graf1.rename(columns={'Trimestre': 'trimestre', 'Valor': 'total'}, inplace=True)
print(graf1.tail(5))
graf1['trimestre'] = graf1['trimestre'].replace(['1º trimestre 2012','2º trimestre 2012','3º trimestre 2012','4º trimestre 2012','1º trimestre 2013','2º trimestre 2013','3º trimestre 2013',\
    '4º trimestre 2013','1º trimestre 2014','2º trimestre 2014','3º trimestre 2014','4º trimestre 2014','1º trimestre 2015','2º trimestre 2015','3º trimestre 2015','4º trimestre 2015',\
        '1º trimestre 2016','2º trimestre 2016','3º trimestre 2016','4º trimestre 2016','1º trimestre 2017','2º trimestre 2017','3º trimestre 2017','4º trimestre 2017','1º trimestre 2018',\
            '2º trimestre 2018','3º trimestre 2018','4º trimestre 2018','1º trimestre 2019','2º trimestre 2019','3º trimestre 2019','4º trimestre 2019','1º trimestre 2020'], ['1ºtri/2012','2ºtri/2012','3ºtri/2012','4ºtri/2012','1ºtri/2013','2ºtri/2013','3ºtri/2013',\
    '4ºtri/2013','1ºtri/2014','2ºtri/2014','3ºtri/2014','4ºtri/2014','1ºtri/2015','2ºtri/2015','3ºtri/2015','4ºtri/2015',\
        '1ºtri/2016','2ºtri/2016','3ºtri/2016','4ºtri/2016','1ºtri/2017','2ºtri/2017','3ºtri/2017','4ºtri/2017','1ºtri/2018',\
            '2ºtri/2018','3ºtri/2018','4ºtri/2018','1ºtri/2019','2ºtri/2019','3ºtri/2019','4ºtri/2019','1ºtri/2020'])
print(graf1)
graf1.to_csv('E:/Área de trabalho/Códigos/R/rs_dados_trabalhoemprego_cargahoraria/data/recossa_cargahoraria_total.csv', index=False)