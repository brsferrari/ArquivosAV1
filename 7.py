import struct
import sys
import os

def quicksort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista)-1

registroSinasc = struct.Struct("6s7s6s8s2s1s4s8s")
with open("sinasc-sp-2018.dat","rb") as f:
    f.seek(0,os.SEEK_END)
    tamanho = f.tell()
    structlength = registroSinasc.size
    n = tamanho // structlength
    
    lines = []
    contador = 0
    fcontador = n
    f.seek(0)
    while contador < fcontador :
        contador += 1
        line = f.read(structlength)
        if len(line) == structlength:
            registro = registroSinasc.unpack(line)
            lines.append(registro)
    lines.sort(key=lambda x:x[1])
    with open ("sinasc-sp-2018-ordenado.dat","w+") as f1:
        f1.write(f"{lines}")