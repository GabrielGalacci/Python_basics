# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')
texto = 'Python'
caracter_entre_letras = '/'
novo_texto = ''
for letra in texto:
    novo_texto += f'{caracter_entre_letras}{letra}'
    print(letra)
print(f'{novo_texto}{caracter_entre_letras}')