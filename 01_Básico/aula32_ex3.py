"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_do_usuario = input('Digite o seu nome de usuário(Primeiro nome): ')
tamanho_nome = len(nome_do_usuario)
nome_curto = tamanho_nome <= 4
nome_normal = (tamanho_nome >= 5) and (tamanho_nome <= 6)
nome_grande = tamanho_nome > 6

if tamanho_nome > 1:
    if nome_curto:
        print(f'{nome_do_usuario} Seu nome é curto!')
    elif nome_normal:
        print(f'{nome_do_usuario} Seu nome é normal!')
    elif nome_grande:
        print(f'{nome_do_usuario} Seu nome é muito grande!')
else:
    print('Digite mais de uma letra!')