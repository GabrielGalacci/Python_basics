# Usando subprocess para executar e comandos externos
# subprocess é um módulo do Python para executar
# processos e comandos externos no seu programa.
# O método mais simples para atingir o objetivo é usando subprocess.run().
# Argumentos principais de subprocess.run():
# - stdout, stdin e stderr -> Redirecionam saída, entrada e erros
# - capture_output -> captura a saída e erro para uso posterior
# - text -> Se True, entradas e saídas serão tratadas como texto
# e automaticamente codificadas ou decodificadas com o conjunto
# de caracteres padrão da plataforma (geralmente UTF-8).
# - shell -> Se True, terá acesso ao shell do sistema. Ao usar
# shell (True), recomendo enviar o comando e os argumentos juntos.
# - executable -> pode ser usado para especificar o caminho
# do executável que iniciará o subprocesso.
# Retorno:
# stdout, stderr, returncode e args
# Importante: a codificação de caracteres do Windows pode ser
# diferente. Tente usar cp1252, cp852, cp850 (ou outros). Linux e
# mac, use utf_8.
# Comando de exemplo:
# Windows: ping 127.0.0.1
# Linux/Mac: ping 127.0.0.1 -c 4

import subprocess
import sys

# Linux: Linux, Linux 2
# MAC: Darwin
# Windows: win32
print(sys.platform)

cmd2 = ['ls', '/']

cmd = ['ping', '127.0.0.1', '-c', '4']
encoding = 'utf_8'
system = sys.platform

if system == "win32":
    cmd = ['ping', '127.0.0.1']
    encoding = 'cp850'


proc = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding=encoding,
    shell=True,
)

proc2 = subprocess.run(
    cmd2, capture_output=True,
    text=True, encoding=encoding,
    shell=True,
)

print()
print('ARGS: ', proc.args)
print('ERRORS: ', proc.stderr)
print('OUTPUT: ', proc.stdout)
print('RETURN: ', proc.returncode)
# print(proc.stdout.decode('cp850')) # Nãu funciona com text = true
print('OUTPUT 2: ', proc2.stdout)
