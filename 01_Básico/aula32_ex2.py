"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_atual = input('Digite a hora(apenas hora) atual: ')

try:
    apenas_hora = int(hora_atual)
    bom_dia = (apenas_hora >= 0) and (apenas_hora <= 11)
    boa_tarde = (apenas_hora >= 12) and (apenas_hora <= 17)
    boa_noite = (apenas_hora >= 18) and (apenas_hora <= 23)

    if (apenas_hora >= 24) or (apenas_hora < 0):
        print(f'{hora_atual} não é uma hora valida!')

    if bom_dia:
        print(f'Agora é {hora_atual} horas. Bom Dia!')
    elif boa_tarde:
        print(f'Agora é {hora_atual} horas. Boa tarde!')
    elif boa_noite:
        print(f'Agora é {hora_atual} horas. Boa noite!')
        
except:
    print('Digite uma hora válida!')
