import requests

#Cores
v = "\033[31m" #Vermelho
verd = "\033[32m" #verde
amar = '\033[33m' #amarelo

def logo():
	print(v+"""

#######                    #                              _______________________
#       # #    # #####    # #   #####  #    # # #    #   |By: Corteisjr          |
#       # ##   # #    #  #   #  #    # ##  ## # ##   #   |Tool: FindAdmin        |
#####   # # #  # #    # #     # #    # # ## # # # #  #   |Date: 1/10/2019        |
#       # #  # # #    # ####### #    # #    # # #  # #   |Contact: +258840109913 |
#       # #   ## #    # #     # #    # #    # # #   ##   |_______________________|
#       # #    # #####  #     # #####  #    # # #    #   
                                                       

""")

def Find():
	site = "\nDigite o nome do site"
	site += "\nPor ex(https//:site.com ou www.site.com ═══━  "
	website = input(verd+site)
	arquivo = open("admin.txt", "r")
	leitura = arquivo.readlines()

	try:
		for leituras in leitura:
			leituras = leituras.replace("\n", "")
			resposta = website+"/"+leituras
			requisicao = requests.get(resposta)
			code = requisicao.status_code

			if code != 301 and code != 404:
				print(v+"[!]Pagina encontrada[!]" + resposta)
				sair = input("Deseja sair [S/N]: ")
				if sair == 's':
					break
			else:
				print(amar+"<<<<<Pagina nao encontrada>>>" + resposta)
	except KeyboardInterrupt:
		print("Saindo")	

flag = True
logo()				

Find()				
