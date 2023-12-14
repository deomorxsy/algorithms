#!/usr/bin/python3
# Árvore Binária utilizando dicionários // Compiladores 3a semana 25/10/2021

arvore = {}

def vazio(aux):
	if len(aux.values()) <= 0:
		return True
	else:
		return False
def criar_arvore(aux,num):
	if vazio(aux):
		aux = {"num": num, "esq":{} ,"dir":{}}
	elif num < aux["num"]:
		aux["esq"] = criar_arvore(aux["esq"], num)
	else:
		aux["dir"] = criar_arvore(aux["dir"], num)
	return aux

def mostrar_EmOrdem(aux):
	if not vazio(aux):
		mostrar_EmOrdem(aux["esq"])
		print(aux["num"], end = ' ')
		mostrar_EmOrdem(aux["dir"])

def consultar_pares(aux):
	if not vazio(aux):
		consultar_pares(aux["esq"])
		if aux["num"] % 2 == 0:
			print(aux["num"], end = ' ')
		consultar_pares(aux["dir"])


while True:
	print("\nMENU DE OPÇÕES - ÁRVORE BINÁRIA\n")
	print("1 - Inserir número")
	print("2 - Consultar números pares")
	print("3 - Consultar toda a árvore em ordem")
	print("4 - Esvaziar a árvore")
	print("5 - Sair")
	op = int(input("Digite sua opção: "))
	if 1 < op > 5:
		print("Opção inválida!!")

	elif op == 1:
		for i in range (0,10):
			num = int(input("Digite o número a ser inserido na árvore: "))
			arvore = criar_arvore(arvore, num)
		print("Números inseridos na árvore!!")

	elif (op == 2):
		if not vazio(arvore):
			consultar_pares(arvore)
		else:
			print("Árvore vazia")

	elif (op == 3):
		if not vazio(arvore):
			mostrar_EmOrdem(arvore)
		else:
			print("Árvore vazia")

	elif (op == 4):
		if not vazio(arvore):
			arvore.clear()
		else:
			print("Árvore vazia")

	elif (op == 5):
		break
