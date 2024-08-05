# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}

uniao = s1 | s2
print(f'{uniao=}')
print()

interseccao = s1 & s2
print(f'{interseccao=}')
print()

diferenca_s1_s2 = s1 - s2
print(f'{diferenca_s1_s2=}')
print()

diferenca_s2_s1 = s2 - s1
print(f'{diferenca_s2_s1=}')
print()

diferenca_simetrica = s1 ^ s2
print(f'{diferenca_simetrica=}')