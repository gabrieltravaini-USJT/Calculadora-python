import os
from re import sub

os.system('cls')

def soma (a,b):
    res = a+b
    return res

def subtracao (c,d):
    res = c-d
    return res

def multi(e,f):
    res = e*f
    return res

def div (g,h):
    res = g/h
    return res
a=4
b=3
c=2
d=1

entrada1 = ''
while 1:
    
    print('Siga as instruções ou digite "sair" para sair.')
    print('-----------------------------------------------------------')    
    entrada1 = input('digite o primeiro operador: ')
    if entrada1 =="sair":
        break

    op = input("digite qual operação vc quer realizar (+,-,* ou /): ")
    if op =="sair":
        break

    entrada2 = input('digite o segundo operador: ')
    if entrada2 =="sair":
        break

    print('-----------------------------------------------------------')
    if op =='+':
        print(soma(int(entrada1),int(entrada2)))
    elif op == '-':
        print(subtracao(int(entrada1),int(entrada2)))
    elif op == '*':
        print(multi(int(entrada1),int(entrada2)))
    elif op == '/':
        if int(entrada2) != 0:
            print(div(int(entrada1),int(entrada2)))
        else:
            print("impossível Dividir por zero")
    else:
        print('Operador inválido')