"""
    Remove propaganda das legendas

"""

import os
import datetime

#os.remove()
#os.rmdir()
diretorio = os.getcwd()

#datetime.

print(diretorio)

#print(os.listdir(diretorio))

for f in os.listdir(diretorio):
    if os.path.isfile(f) & f[-4:].endswith("srt"):
        #print(f[-4:])
        with open(f) as fil:
            print(f)
            print(fil)
            print(fil.read(5))
            print("----------Fim do arquivo ---------")