#!/usr/bin/python3
import sys # to exit with security

class binaryTree:
    # creating a new node, the node_obj is the object this node will hold.
    def __init__(self, root_obj):
        self.node_obj = root_obj
        self.left_child = None
        self.right_child = None

#tree = binaryTree('a')
#print(tree.node_obj)
#print(tree.left_child)
#print(tree.right_child)
    '''
    Regras para a inserção:

    primeiramente é checado o valor da root. Se o valor a ser adicionado é menor ou igual ao valor da root,
    o valor é atribuido a left_child da root. Se for maior, adiciona o valor ao node da direita.

    protótipo left e right

    #===========

    def leftInsert(self, node_obj):
        if self.left_child == None:
            self.left_child = binaryTree(node_obj)
        else:
            add_child = binaryTree(node_obj) # Instanciação de objeto binaryTree chamado "add_child" e atribuição dessa instância a uma variável
            add_child.left_child = self.left_child # atribuição da variável da classe SELF a uma variável
            self.left_child = add_child # criar um objeto dentro de uma classe que chama a própria classe utiliza recursão e é similar a ideia de ponteiro para ponteiro.

    def rightInsert(self, node_obj):
        if self.right_child == None:
            self.right_child = binaryTree(node_obj)
        else:
            add_child = binaryTree(node_obj)
            add_child.right_child = self.right_child
            self.right_child = add_child
     #===========
     '''

     def insertNode(self, node_obj):
        # left_child
        if node_obj <= (self.node_obj and self.left_child):
            self.left_child.insert_node(node_obj)
        elif node_obj <= self.node_obj:
            self.left_child = binaryTree(node_obj)
        # right_child
        elif node_obj > (self.node_obj and self.right_child):
            self.right_child.insert_node(node_obj)
        elif node_obj <= self.node_obj:
            self.right_child = binaryTree(node_obj)

    def buscador(self, valor):
        if valor < self.valor and self.left_child:
            return self.left_child.buscador(valor) # instanciando o método de forma recursiva
        if valor > self.valor and self.right_child:
            return self.right_child.buscador(valor)
        return valor == self.valor # True or False: checa se o valor pesquisado é um dos valores inseridos nos nodes

def main():

    somosnozes = binaryTree(0) # instanciamento da classe binaryTree

    print("\nMENU DE OPÇÕES - ÁRVORE BINÁRIA\n");
    print("1 - Inserir número");
    print("2 - Consultar números pares");
    print("3 - Consultar toda a árvore em ordem");
    print("4 - Esvaziar a árvore");
    print("5 - Sair");
    entrada = input("Digite sua opção: ");

    if entrada == 1:
        numero = input("Digite o número que quer inserir na árvore: ")
        somosnozes.insertNode(numero)

    elif entrada == 2:
        numero = input("Digite o número que quer inserir na árvore: ")
        if buscador(numero) / 2 == 0:
            print(somosnozes.buscador(numero))

    elif entrada == 3:
        #Depth-First Search:procura em profundidade
        numero = input("Digite o número que quer inserir na árvore: ")
        somosnozes.buscador(numero)

    elif entrada == 4:
        do x
    elif entrada == 5:
        Sys.exit("flwssssssssssss")


if __name__ == "__main__":
    main()
