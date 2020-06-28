#preciso rever o teste, está com a versão antiga do teste. Ou seja, preciso refazer!!!
import jogovelha
import sys

erroMenu = False


jogo = jogovelha.menu()

if len(jogo) != 3:
	erroMenu = True
else:
	for linha in jogo:
		if len(linha) != 3:
			erroMenu = True
		else:
			for elemento in linha:
				if elemento != '.':
					erroMenu = True
if erroMenu:
	sys.exit(1)
else:
	sys.exit(0)
