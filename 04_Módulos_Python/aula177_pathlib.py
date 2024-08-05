from pathlib import Path
from shutil import rmtree

caminho_projeto = Path()
# print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)
# print(caminho_arquivo.parent)
# print(caminho_arquivo.parent.parent)

ideias = caminho_arquivo.parent / 'ideias'
# print(Path.home())

# arquivo.touch() # Criar o arquivo

# arquivo.unlink() # Apaga o arquivo

# arquivo.write_text('Olá Mundo¹') # Escreve no arquivo texto simples
# arquivo.write_text('Hello World¹') # Sobrescreve o de cima

# Para escrever mais textos utilizar o comando
# with caminho_arquivo.open('a+') as file:
#     file.write('Uma linha')
#     file.write('Outra linha')

# arquivo.read_text() # Lê o que está no arquivo

caminho_pasta = Path.home() / 'Área de Trabalho'/ 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('Hey You!')

# caminho_pasta.rmdir() # Para usar o comando é necessário apagar as pastas internas

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
    
    if file.exists():
        file.unlink()
    else:
        file.touch()
        
    with file.open('a+') as text_file:
        text_file.write('Olá mundo')
        text_file.write(f'file_{i}.txt')
        
# rmtree(caminho_pasta) # Usando shutil

def rmtree_(root, remove_root=True):
    for file in root.glob('*'):
        if file.isdir():
            rmtree_(file, False)
            file.rmdir()
        else:
            file.unlink()    
    
    if remove_root:
        root.rmdir()
        
rmtree(caminho_pasta) # NÃO MODIFICAR