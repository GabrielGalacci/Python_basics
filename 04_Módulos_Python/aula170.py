# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'

import os

caminho = os.path.join(
    'C:', '\\Users', 'gabri', 'OneDrive', 'Área de Trabalho',
    'Curso_Python', '04_Módulos_Python'
)

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)
    
    if not os.path.isdir(caminho_completo_pasta):
        continue
    
    for arquivo in os.listdir(caminho_completo_pasta):
        print('   ', arquivo)
