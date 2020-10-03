"""
Script para Organizar pasta de downloads de series
Busca arquivos de videos nos folders, apaga os arquivos .exe e .nfo
"""

import os
import shutil

home_dir = os.getcwd()
home_lista = os.listdir(home_dir)

def move_arq(path_diretorio):
    """Faz a busca nos recursivas em diretorios filhos e move todos os arquivos de video para o diretorio de trabalho

    Args:
        path_diretorio (Path.String): Path do sistema em String
    """
    lista_def = os.listdir(path_diretorio)
    for lst_def in lista_def:
        lst_for = path_diretorio + os.sep + lst_def
        if os.path.isfile(lst_for):
            extensao = lst_for[lst_for.rindex(".") + 1:]
            if extensao in ("mp4", "mkv"):
                try:
                    shutil.move(path_diretorio + os.sep + lst_def, home_dir)
                except:
                    print("Erro ao copiar arquivo")
            elif extensao in ("nfo", "jpg", "png", "exe", "txt"):
                try:
                    os.remove(lst_for)
                except:
                    print("Erro ao apagar arquivo")
        
        elif os.path.isdir(path_diretorio +os.sep + lst_def):
            move_arq(path_diretorio+ os.sep +lst_def)
            try:
                os.rmdir(path_diretorio(path_diretorio+ os.sep +lst_def))
                pass
            except:
                print("Erro ao apagar o Diretório")
                pass

for lst in home_lista:
    if os.path.isdir(lst):
        move_arq(home_dir+ os.sep +lst)
