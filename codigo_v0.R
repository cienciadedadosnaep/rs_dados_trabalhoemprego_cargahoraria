######################################################
# 1) Carregar bibliotecas

library(tidyverse)
library(magrittr)
#library(dplyr)
library(readr)
library(rjson)
library(RJSONIO)

# # Library para importar dados SQL
# library(DBI)
# library(RMySQL)
# library(pool)
# library(sqldf)
# library(RMariaDB)
# 
# # Carragamento de banco de dados
# 
# # Settings
# db_user <-'admin'
# db_password <-'password'
# db_name <-'cdnaep'
# #db_table <- 'your_data_table'
# db_host <-'127.0.0.1' # for local access
# db_port <-3306
# 
# # 3. Read data from db
# # drv=RMariaDB::MariaDB(),
# mydb <-  dbConnect(drv =RMariaDB::MariaDB(),user =db_user, 
#                    password = db_password ,
#                    dbname = 'cdnaep', host = db_host, port = db_port)
# 
# dbListTables(mydb)
# 
# s <- paste0("SELECT * from", " consumo_agua")
# rs<-NULL
# rs <- dbSendQuery(mydb, s)
# 
# dados<- NULL
# dados <-  dbFetch(rs, n = -1)
# dados
# #dbHasCompleted(rs)
# #dbClearResult(rs)

library(readr)
dados <- read_csv("data/recossa_cargahoraria_total.csv")
names(dados)
nomes <- names(dados)
nomes[2] = 'Total'
##  Perguntas e titulos 
T_ST_P_No_TRABALHOEMPREGO <- read_csv("data/TEMA_SUBTEMA_P_No - TRABALHOEMPREGO.csv")


#dados <- dados %>% add_column(valor = 'valor', .after = 'trimestre')

#dados %<>% gather(key = classe,
#                  value = valor,-trimestre,-Homens) 


#dados %<>% select(-id)
# Temas Subtemas Perguntas



## Arquivo de saida 

SAIDA_POVOAMENTO <- T_ST_P_No_TRABALHOEMPREGO %>% 
  select(TEMA,SUBTEMA,PERGUNTA,NOME_ARQUIVO_JS)
SAIDA_POVOAMENTO <- as.data.frame(SAIDA_POVOAMENTO)

#classes <- NULL
#classes <- levels(as.factor(dados$classe))

# Cores secundarias paleta pantone -
corsec_recossa_azul <- c('#a094e1','#dc6f6c','#62acd1','#8bc6d2',
                         '#d62839','#20cfef','#fe4641','#175676')
# Cor 1 - Roxo; Cor 2, 5, 7 - Vermelho; Cor 3, 4, 6, 8 - Azul

simbolo_linhas <- c('emptyCircle','emptyTriangle','emptySquare',
                    'emptyDiamond','emptyRoundRect')

#for ( i in 1:length(classes)) {

objeto_0 <- dados %>%
  #filter(classe %in% c(classes[1])) %>%
  select(trimestre,total) %>% #filter(ano<2019) %>%
  #arrange(trimestre) %>%
  mutate(trimestre = as.character(trimestre)) %>% list()               

exportJson0 <- toJSON(objeto_0)


titulo<-T_ST_P_No_TRABALHOEMPREGO$TITULO[1]
subtexto<-"Fonte: SIDRA IBGE"
link <- T_ST_P_No_TRABALHOEMPREGO$LINK[1]

data_axis <- paste('["',gsub(' ','","',
                             paste(paste(as.vector(objeto_0[[1]]$trimestre)),
                                   collapse = ' ')),'"]',sep = '')


data_serie <- paste('[',gsub(' ',',',
                             paste(paste(as.vector(objeto_0[[1]]$total)),
                                   collapse = ' ')),']',sep = '')

#Colocar o nome da coluna depois de "objeto_0[[1]]$"

texto<-paste('{"title":{"text":"',titulo,
             '","subtext":"',subtexto,
             '","sublink":"',link,'"},',
             '"tooltip":{"trigger":"axis"},',
             '"toolbox":{"left":"center","orient":"horizontal","itemSize":20,"top":20,"show":true,',
             '"feature":{"dataZoom":{"yAxisIndex":"none"},',
             '"dataView":{"readOnly":false},',
             '"restore":{},"saveAsImage":{}}},"legend":{"show":true,"bottom":30},"grid":{"bottom":80},"xAxis":{"type":"category",',
             '"data":',data_axis,'},',
             '"yAxis":{"type":"value","axisLabel":{"formatter":"{value}"}},',
             '"graphic":[{"type":"text","left":"center","top":"bottom","z":100, "style":{"fill":"gray","text":"Obs: Ponto é separador decimal", "font":"8px sans-srif","fontSize":12}}],',
             '"series":[{"name":"',nomes[2],'","data":',data_serie,',',
             '"type":"line","color":"',corsec_recossa_azul[7],'","showBackground":true,',
             '"backgroundStyle":{"color":"rgba(180, 180, 180, 0.2)"},"symbol":"',simbolo_linhas[5],
             '","symbolSize":10,"itemStyle":{"borderRadius":10,"borderColor":"',corsec_recossa_azul[7],'","borderWidth":2}}',
             ']}',sep='')

#SAIDA_POVOAMENTO$CODIGO[i] <- texto   
texto<-noquote(texto)


write(exportJson0,file = paste('data/',gsub('.csv','',T_ST_P_No_TRABALHOEMPREGO$NOME_ARQUIVO_JS[1]),
                               '.json',sep =''))
write(texto,file = paste('data/',T_ST_P_No_TRABALHOEMPREGO$NOME_ARQUIVO_JS[1],
                         sep =''))

#}

# Arquivo dedicado a rotina de atualizacao global. 

write_csv2(SAIDA_POVOAMENTO,file ='data/POVOAMENTO.csv',quote='all',escape='none')
#quote="needed")#,escape='none')


objeto_autm <- SAIDA_POVOAMENTO %>% list()
exportJson_aut <- toJSON(objeto_autm)

#write(exportJson_aut,file = paste('data/povoamento.json'))