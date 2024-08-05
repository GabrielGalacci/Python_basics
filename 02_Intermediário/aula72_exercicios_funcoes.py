# Exercícios com funções

# Crie um função que multiplica todos os argumentos
# não nomeados recebidos
# retorne o total para uma variável e mostre o valor
# da variável

def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado
    
multiplicacao = multiplicar(1, 2, 5, 10, 1, 5)
print(multiplicacao)

# Crie uma função que fale se o número é par ou ímpar.
# Retorne se o número é par ou ímpar

def paridade(x):
    numero = int(x)

    if numero % 2 == 0:
        return 'Par'
    return 'Ímpar'
    
numero_digitado = input('Digite um número: ')
teste_paridade = paridade(numero_digitado)

print(f'{numero_digitado} é: {teste_paridade}')

