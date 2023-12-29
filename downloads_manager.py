import os

def create_sub_dirs(main_dir: str):
    try:
        os.makedirs(f'{main_dir}imagens')
    except FileExistsError:
        pass
    try:
        os.makedirs(f'{main_dir}vídeos')
    except FileExistsError:
        pass
    try:
        os.makedirs(f'{main_dir}áudios')
    except FileExistsError:
        pass
    try:
        os.makedirs(f'{main_dir}documentos')
    except FileExistsError:
        pass

while True:
    downloads_dir = str(input('Digite o caminho do diretório de downloads: '))
    if downloads_dir == '':
        print('\033[91mO caminho está vazio! Insira um caminho válido!\033[0m')

    elif not os.path.isdir(downloads_dir):
        print(f'\033[91mO caminho `{downloads_dir}` não é uma pasta\033[0m')
    
    elif downloads_dir[len(downloads_dir) - 1] != '/':
        print(f'\033[91mO caminho `{downloads_dir} deve conter uma / no final.`')

    elif not os.path.exists(downloads_dir):
        print(f'\033[91mO caminho `{downloads_dir}` não foi encontrado.\033[0m')

    else:
        print(f'\033[92m`{downloads_dir}` foi validado com sucesso!\033[0m')
        break

create_sub_dirs(downloads_dir)
