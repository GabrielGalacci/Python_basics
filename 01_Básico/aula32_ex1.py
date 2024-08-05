"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_digitado = input('Digite um Número inteiro: ')

try:
    numero_inteiro = int(numero_digitado)
    numero_par = (numero_inteiro % 2) == 0

    if numero_par:
        print(f'O número {numero_digitado} é par!')
    else:
        print(f'O número {numero_digitado} é ímpar!') 

except:
    print("Você não digitou um número inteiro!")