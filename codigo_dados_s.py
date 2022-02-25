import pandas as pd

df = pd.read_json('http://api.sidra.ibge.gov.br/values/t/6371/n6/2927408/v/8186,8188,8190,8192/p/all/c2/allxt?formato=json')
#df.info()
selecao = 'Média de horas habitualmente trabalhadas por semana no trabalho principal das pessoas de 14 anos ou mais de idade'
grafico = df[["D3N","V","D2N","D4N"]]
grafico1 = grafico[grafico['D2N']==selecao]
grafico1 = grafico1[grafico['D4N']=='Homens']
grafico2 = grafico[grafico['D2N']==selecao]
grafico2 = grafico2[grafico['D4N']=='Mulheres']
#grafico.info()
#print(grafico.head(5))
graf1 = grafico1[['D3N','V']].reset_index(drop=True)
graf2 = grafico2[['D3N','V']].reset_index(drop=True)
#print(grafico1.head(5))
#print(grafico2.head(5))
#graf2.info()
#print(graf2.tail(10))
graf1 = graf1.drop([33,34,35,36,37,38,39])
graf2 = graf2.drop([33,34,35,36,37,38,39])
#print(graf2.tail(10))
graf1.rename(columns={'D3N': 'trimestre', 'V': 'Homens'}, inplace=True)
graf2.rename(columns={'D3N': 'trimestre', 'V': 'Mulheres'}, inplace=True)
print(graf1.tail(5))
print(graf2.tail(5))
#print(graf2.head(5))
graf1['trimestre'] = graf1['trimestre'].replace(['1º trimestre 2012','2º trimestre 2012','3º trimestre 2012','4º trimestre 2012','1º trimestre 2013','2º trimestre 2013','3º trimestre 2013',\
    '4º trimestre 2013','1º trimestre 2014','2º trimestre 2014','3º trimestre 2014','4º trimestre 2014','1º trimestre 2015','2º trimestre 2015','3º trimestre 2015','4º trimestre 2015',\
        '1º trimestre 2016','2º trimestre 2016','3º trimestre 2016','4º trimestre 2016','1º trimestre 2017','2º trimestre 2017','3º trimestre 2017','4º trimestre 2017','1º trimestre 2018',\
            '2º trimestre 2018','3º trimestre 2018','4º trimestre 2018','1º trimestre 2019','2º trimestre 2019','3º trimestre 2019','4º trimestre 2019','1º trimestre 2020'], ['1ºtri/2012','2ºtri/2012','3ºtri/2012','4ºtri/2012','1ºtri/2013','2ºtri/2013','3ºtri/2013',\
    '4ºtri/2013','1ºtri/2014','2ºtri/2014','3ºtri/2014','4ºtri/2014','1ºtri/2015','2ºtri/2015','3ºtri/2015','4ºtri/2015',\
        '1ºtri/2016','2ºtri/2016','3ºtri/2016','4ºtri/2016','1ºtri/2017','2ºtri/2017','3ºtri/2017','4ºtri/2017','1ºtri/2018',\
            '2ºtri/2018','3ºtri/2018','4ºtri/2018','1ºtri/2019','2ºtri/2019','3ºtri/2019','4ºtri/2019','1ºtri/2020'])
graf2['trimestre'] = graf2['trimestre'].replace(['1º trimestre 2012','2º trimestre 2012','3º trimestre 2012','4º trimestre 2012','1º trimestre 2013','2º trimestre 2013','3º trimestre 2013',\
    '4º trimestre 2013','1º trimestre 2014','2º trimestre 2014','3º trimestre 2014','4º trimestre 2014','1º trimestre 2015','2º trimestre 2015','3º trimestre 2015','4º trimestre 2015',\
        '1º trimestre 2016','2º trimestre 2016','3º trimestre 2016','4º trimestre 2016','1º trimestre 2017','2º trimestre 2017','3º trimestre 2017','4º trimestre 2017','1º trimestre 2018',\
            '2º trimestre 2018','3º trimestre 2018','4º trimestre 2018','1º trimestre 2019','2º trimestre 2019','3º trimestre 2019','4º trimestre 2019','1º trimestre 2020'], ['1ºtri/2012','2ºtri/2012','3ºtri/2012','4ºtri/2012','1ºtri/2013','2ºtri/2013','3ºtri/2013',\
    '4ºtri/2013','1ºtri/2014','2ºtri/2014','3ºtri/2014','4ºtri/2014','1ºtri/2015','2ºtri/2015','3ºtri/2015','4ºtri/2015',\
        '1ºtri/2016','2ºtri/2016','3ºtri/2016','4ºtri/2016','1ºtri/2017','2ºtri/2017','3ºtri/2017','4ºtri/2017','1ºtri/2018',\
            '2ºtri/2018','3ºtri/2018','4ºtri/2018','1ºtri/2019','2ºtri/2019','3ºtri/2019','4ºtri/2019','1ºtri/2020'])
print(graf1)
print(graf2)
graf2 = graf2[['Mulheres']]
graf = pd.concat([graf1,graf2], axis=1)
print(graf)
graf.to_csv('E:/Área de trabalho/Códigos/R/rs_dados_trabalhoemprego_cargahoraria/data/recossa_cargahoraria_s.csv', index=False)


