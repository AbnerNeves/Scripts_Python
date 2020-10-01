"""
    Remove propaganda das legendas

"""

import os
import datetime

home_dir = os.getcwd()

print(home_dir)

def busca_srt(diretorio):
    """
    Faz a busca no diretorio por arquivos .srt, abre e procura a propaganda, e substitui por ""

    Args:
        diretorio (path.directory): Pasta do sistema onde será feita a busca por arquivos .srt
    """
    for arquivo in os.listdir(diretorio):
        if os.path.isfile(diretorio + os.sep + arquivo) and arquivo.endswith("srt"):
            with open(diretorio + os.sep + arquivo) as leitura:
                linhas = leitura.readlines(150)
                # print(linhas)
                # tamanho = 0
                for item in linhas:
                    if "OpenSubtitles" or "Anuncie seu produto ou marca aqui" in item:
                        print("achei")
                    # tamanho = tamanho + len(linhas)
                    # print(item)
                    # print(type(item))
                    pass
                # print(tamanho)
                leitura.close()
                pass

    pass


for f in os.listdir(home_dir):
    if os.path.isdir(f):
        busca_srt(home_dir + os.sep + f)