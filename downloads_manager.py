from shutil import move
from os import makedirs, path, listdir
from time import sleep

while True:
    downloads_dir = str(input('Digite o caminho do diretório de downloads: '))
    if downloads_dir == '':
        print('\033[91mO caminho está vazio! Insira um caminho válido!\033[0m')

    elif not path.exists(downloads_dir):
        print(f'\033[91mO caminho `{downloads_dir}` não foi encontrado.\033[0m')

    elif not path.isdir(downloads_dir):
        print(f'\033[91mO caminho `{downloads_dir}` não é uma pasta\033[0m')

    else:
        print(f'\033[92m`{downloads_dir}` foi validado com sucesso!\033[0m')
        break

file_types = {
    '.jpg': 'Imagens',
    '.jpeg': 'Imagens',
    '.svg': 'Imagens',
    '.png': 'Imagens',
    '.gif': 'Imagens',
    '.bmp': 'Imagens',
    '.mp4': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',
    '.mov': 'Videos',
    '.wmv': 'Videos',
    '.flv': 'Videos',
    '.mpg': 'Videos',
    '.mpeg': 'Videos',
    '.mp3': 'Audios',
    '.wav': 'Audios',
    '.flac': 'Audios',
    '.aac': 'Audios',
    '.ogg': 'Audios',
    '.m4a': 'Audios',
    '.wma': 'Audios',
    '.aif': 'Audios',
    '.aiff': 'Audios',
    '.pdf': 'Documentos',
    '.doc': 'Documentos',
    '.docx': 'Documentos',
    '.txt': 'Documentos',
    '.pptx': 'Documentos',
    '.xlsx': 'Documentos',
    '.*': 'Outros',
}

for file_type in file_types.values():
    dir = path.join(downloads_dir, file_type)
    if not path.exists(dir):
        makedirs(dir)

files = listdir(downloads_dir)
for file in files:
    file_path = path.join(downloads_dir, file)
    if path.isfile(file_path):
        name, extension = path.splitext(file)
        extension = extension.lower()

        if extension in file_types:
            destiny = path.join(downloads_dir, file_types[extension])
        else:
            destiny = path.join(downloads_dir, 'Outros', file)

        move(path.join(downloads_dir, file), destiny)
        sleep(2)
        try:
            print(f'\n\033[92mArquivo {file} movido para {file_types[extension]}.\033[0m\n')
        except KeyError:
            print(f'\n\033[38;5;208mArquivo {file} movido para o diretório Outros\033[0m\n')

print('\033[94mTODOS OS ARQUIVOS FORAM MOVIDOS COM SUCESSO!\033[0m')
