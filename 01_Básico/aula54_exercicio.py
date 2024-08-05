"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista.
Não permita que a lista quebre com
erros de índices inexistentes na lista.
"""
import os

lista_de_compras = []

while True:
    acoes_permitidas = 'ial'
    acao = input('Selecione uma opção\n[i]nserir [a]pagar [l]istar: ').lower()

    if acao not in acoes_permitidas:
        print('Insira uma opção dentre as permitidas!')
        continue

    if acao == 'i':
        os.system('cls')

        item_inserido = input('O que você deseja adicionar? ')
        inserir_item = lista_de_compras.append(item_inserido)
        
    elif acao == 'a':
        indice_apagar = input('Escolha o índice para apagar: ')

        try:
            indice_apagar_int = int(indice_apagar)
            del lista_de_compras[indice_apagar_int]
        except ValueError:
            print('Por favor digite um número inteiro!')
            continue
        except IndexError:
            print('O índice digitado não existe na lista!')
        except Exception:
            print('Erro desconhecido!')

    elif acao == 'l':
        os.system('cls')
        
        if len(lista_de_compras) == 0:
            print('Não tem nada para listar!')

        for indice, item in enumerate(lista_de_compras):
            print(indice, item)

            
