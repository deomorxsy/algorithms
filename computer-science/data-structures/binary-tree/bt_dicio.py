#!/usr/bin/python3

raiz = {}

def vazio(arvore):
    if (len(aux.values()) <= 0):
        return True
    else:
        return False


def inserirArvore(aux, num):
    if (vazio(aux)):
        aux = {"num": num, "esq": {}, "dir": {} }
    elif(num <= aux["esq"]):
        aux["esq"] = inserArvore(aux["esq"], num)
    else
        aux["dir"] = inserArvore(aux["dir"], num)
    return aux

def mostrarOrdem(aux):
    if(not vazio(aux)):
        mostrarOrdem(aux["esq"])
        print(aux["num"], end=" ")
        mostrarOrdem(aux["dir"])

def mostrarPares(aux):
    if(not vazio(aux)):
        mostrarPares(aux["esq"])
        if (aux["num"] % 2 == 0):
            print(aux["num"], end=" ")
        mostrarPares(aux["dir"])

while (opt != 5):
    System.out.println("\nMENU DE OPÇÕES - ÁRVORE BINÁRIA\n");
    System.out.println("1 - Inserir número");
    System.out.println("2 - Consultar números pares");
    System.out.println("3 - Consultar toda a árvore em ordem");
    System.out.println("4 - Esvaziar a árvore");
    System.out.println("5 - Sair");
    System.out.print("Digite sua opção: ");

    opt = int(input("Digite sua opção: "))
    if (1 < opt > 5):
        print("Opção Inválida")
    elif (opt == 1):
        raiz = inserirArvore(aux, int(input("Digite um número: "))):
    elif (opt == 2):
        if (vazio(raiz)):
            print("Árvore vazia")
        else:
            mostrarPares(raiz)
    elif (opt == 3):
        if(vazio(raiz)):
            print("Árvore vazia")
        else:
            mostrarOrdem(raiz)
    elif (opt == 4):
        if (not vazio(raiz)):
            raiz.clear()
    elif (opt == 5):
        break


#raiz = inserirArvore(raiz, 6) #{"num": 6, "esq": {}, "dir": {}}
#raiz = inserirArvore(raiz, 4)
#print(raiz)




