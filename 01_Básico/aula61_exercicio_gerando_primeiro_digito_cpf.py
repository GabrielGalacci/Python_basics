"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '412887078'
cpf_sem_ponto = (cpf.split('.'))
cpf_sem_ponto_junto = ''.join(cpf_sem_ponto)
nove_digitos = cpf_sem_ponto_junto[:9]

soma_da_multiplicacao_1 = 0

contagem_regressiva_1 = 10

for digito in nove_digitos:
    multiplicacao_dos_digitos = int(digito) * contagem_regressiva_1
    soma_da_multiplicacao_1 += multiplicacao_dos_digitos
    contagem_regressiva_1 = contagem_regressiva_1 - 1

digito_validacao_1 = (soma_da_multiplicacao_1*10) % 11

digito_validacao_1 = digito_validacao_1 if digito_validacao_1 <= 9 else 0
print(digito_validacao_1)
