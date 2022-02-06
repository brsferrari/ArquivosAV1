from atexit import register
import struct
import sys
import os

registroSinasc = struct.Struct("6s7s6s4s4s2s1s4s8s")
with open("sinasc-sp-2018.dat","rb") as f:
    f.seek(0,os.SEEK_END)
    tamanho = f.tell()
    structlength = registroSinasc.size
    n = tamanho // registroSinasc.size

    #Busca Sequencial
    contador = 0
    contador2 = 0
    contador3 = 0
    fcontador = n
    f.seek(0)
    while contador < fcontador :
        contador += 1
        line = f.read(structlength)
        if len(line) == structlength:
            registro = registroSinasc.unpack(line)
            codmunnasc = registro[0].decode()
            ano = registro[4].decode()
            sexo = registro[6].decode()
            peso = registro[8].decode()
        if codmunnasc == "354850" and ano == "2018" and sexo == "2":
            contador2 += 1
        if codmunnasc == "350950" and ano == "2018" and peso < "2500":
            contador3 += 1
 
    print(f"{contador2}")
    print(f"{contador3}")