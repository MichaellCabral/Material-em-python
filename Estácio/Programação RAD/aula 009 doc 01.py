import os

def menu():
    escoha = 0
    while (escolha!=5):
        print("1- Adição")
        print("2- Subtração")
        print("3- Multiplicação")
        print("4- Divisão")
        print("5- Sair")
        escoha = int(input("faça sua escolha"))

        if escolha == 1:
            (op1,op2)=entrada_dados()
            resultado = adição(op1,op2)
        elif escolha == 2
        