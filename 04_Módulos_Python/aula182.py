# Secrets gera números aleatórios seguros

import secrets
import string as s
from secrets import SystemRandom as Sr

print(
    'SENHA 20 CARACTERES: ', ''.join(
        Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=20)
    )
)

# COMANDO PARA USAR NO PROMPT PARA USAR O SUSTEMA ABAIXO
# python -c "import string as s;from secrets import SystemRandom as Sr;
# print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"

random = secrets.SystemRandom()


# O seed não faz nada com o uso de secrets

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 200, 2)
print('RANDRANGE: ', r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
print('RANDINT: ', r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
print('UNIFORM: ', r_uniform)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Gabriel', 'Maria', 'Helena', 'Joana']
print('NOMES: ', nomes)
random.shuffle(nomes)
print('SHUFFLE: ', nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes1 = random.sample(nomes, k=3)
print('NOVOS NOMES COM SAMPLE: ', novos_nomes1)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes2 = random.choices(nomes, k=3)
print('NOVOS NOMES COM CHOICES: ', novos_nomes2)

# random.choice(Iterável) -> Escolhe um elemento do iterável
print('CHOICE: ', random.choice(nomes))


