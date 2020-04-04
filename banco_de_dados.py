							# Inicio do codigo
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Psycopg2 é o comunicador com o PostgreSQL
from psycopg2 import connect
# Sys para se comunicar com algumas funçoes do shell OS
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
#OS é a conversa do python com o Windows 
import os
# time são comandos de tempo , como colocar o python para esperar " time.sleep()""
import time
# Shutil é para manipular arquivos no windows, como criar diretorios , copiar arquivo de um lugar para o outro 
import shutil
# uma INTERFACE simples que usei para poder nao deixar tão sem resposta o cliente no time.sleep()
import PySimpleGUI as sg
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
retval = os.getcwd() # Comanmdo para o python verificar a pasta que ele se encontra / está sendo executado
db_name_limpo = "\\mybkup.backup" # dei esse nome a variavel para eu chamar ela como string formatada.
shutil.copy(f"{retval}"+f"{db_name_limpo}" , "C:\\folder") # Estou fazendo uma copia onde ele vai usar a variavel que pedi pro python ver a onde ele está , fiz a concatenação com a variavel do nome do arquivo backup, em seguinda com , pedi pra ele copiar no local já fixo definido

pasta   = str(input("Defina o nome da pasta: ")) # Solicito ao usuario dar o nome a nova pasta que vai ser criada
os.chdir("C:\\folder") # Peço pro python ir nesse diretorio que eu defini
shutil.copytree("C:\\folder\\folder",f"C:\folder\\{pasta}") # Solicito ao python fazer copia da pasta para a nova pasta com o nome que o usuario definio
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Comando para gerar a GUI como se fosse o time.sleep porém com interface , para nao ficar algo parado ao cliente.
mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
for i, item in enumerate(mylist):
    sg.one_line_progress_meter('Copiando a pasta!!', i+1, len(mylist), '-key-')
    time.sleep(1)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
db_novo   = str(input("Digite o nome do database: ")) # Solicito ao usuario que defina o nome do novo banco de dados que será criado

db   	  = open(f"C:\\folder\\{pasta}\\Config.ini","w+") # O python vai abrir o arquvio .ini como permissão de leitura e escrita (w+)
for i in range(1): # Aqui eu vou pedir pra ele escrever só uma vez
	db.write(f"[Conexao]\nDriver=PG\nHost=127.0.0.1\nDatabase={db_novo}\nPorta=5434\nUsuario=postgres\nVersaoFB=30") # Peço então pra ele escrever , achei mais facil assim do que tentar fazer o python procurar a linha que eu desejo dentro do arquivo e mudar somente a opçao. Como o texto é fixo assim da menos trabalho
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

con   = None # Defini a variavel como tipo NULL
con   = connect(dbname='postgres',user='postgres', host = 'localhost', password='my_pass_word',port=5434) # Chamei um comando do psycopg2 on de eu solicito uma conexão no banco de dados 
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # Defino a isolaçao do codigo para nao dar nenhum problema , como se fosse privilegio para ele dar continuidade 

cur   = con.cursor() # Aberto um cursor para realizar os procedimentos no banco de dados , usando comando de SQL
cur.execute('CREATE DATABASE ' + db_novo) # Comando de SQL para criar um novo banco de dados, fiz a concatenação com o input do usuario
cur.close() # Fechando o comando cursor	

con.close() # Fechando a conexão
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
novo_bat  = open("C:\\folder\\PostgreSQL\\bin\\restore.bat","w") # Aqui esotu pedindo pra o python verificar se existe restore.bat criado , caso contrario ele vai criar
novo_bat.write(f'pg_restore.exe -h localhost -p 5434 -U postgres -d {db_novo} -v "c:\\folder\\mybkup.backup"') # Peço para o Python criar esses comando no .bat,  usando a formataçao com a variavel que é o input de banco de dados que o usuario colocou
novo_bat.close() # Solicito ao python para salvar e fechar o arquivo
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
os.chdir("C:/folder/PostgreSQL/bin") # Peço para o python ir nesse diretorio
os.startfile("restore.bat") # Peço ao python que execute o arquivo que se encontra nele já definido na variavel novo_bat

time.sleep(10) # Peço para o python aguaradar 10 segundos antes de executar o proximo codigo , pois irá abrir um CMD do POSTGRESQL solicitando senha para dar continuidade com o restore do backup
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Mais uma vez para o cliente não ficar sem nada interativo na tela , eu subi isso enquanto ele aguardar!
mylist1  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
for i, item in enumerate(mylist1):
    sg.one_line_progress_meter('Ajustando DataBase - Aguarde!!', i+1, len(mylist1), '-key-')
    time.sleep(1)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
os.chdir(f"C:/folder/{pasta}") # Peço para o Python ir até essa pasta, ja existe uma variavel chamado pasta que foi definida o nome pelo o usuario
os.startfile("my_project.exe") # Peço para ele executar o arquivo que se encontra dentro dessa pasta

time.sleep(10) # Peço para o Python aguardar 10 segundos até executar  o proximo bloco de codigo
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
atalho   	 = str(input("Define o nome do atalho: ")) # Input para o cliente definir o nome do atalho que será criado
atalho_bat   = open(f"C:\\folder\\{pasta}\\atalho.bat","w") # O python irá verificar se está criado o .bat, caso contrario irá criar
atalho_bat.write(f'@echo off\n\nset SCRIPT="%TEMP%\\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"\n\necho Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%\necho sLinkFile = "%USERPROFILE%\\Desktop\\{atalho}.lnk" >> %SCRIPT%\necho Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%\necho oLink.TargetPath = "C:\\folder\\{pasta}\\myapp.exe" >> %SCRIPT%\necho oLink.Save >> %SCRIPT%\n\ncscript /nologo %SCRIPT%\ndel %SCRIPT%') # Conteudo do .bat 
atalho_bat.close() # Peço para ele fechar e salvar .bat
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
os.chdir(f"C:/folder/{pasta}") # Solicito ao python para ele nesse diretorio , com a variavel pasta já definida
os.startfile("atalho.bat") # Peço para executar o .bat
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                #Fim da Execução do Codigo
