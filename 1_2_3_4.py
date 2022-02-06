import struct
import sys
import os

#Estrutura do meu arquivo de dados
registroSinasc = struct.Struct("6s7s6s8s2s1s4s8s")

#Abrindo o arquivo para leitura como f
with open("sinasc-sp-2018.dat","rb") as f:
    #Anda com o curso do começo ao fim do arquivo e retorna seu tamanho
    f.seek(0,os.SEEK_END)
    tamanho = f.tell()
    print( f"Tamanho do arquivo: {tamanho}")

    #Tamanho dos registros
    structlength = registroSinasc.size
    print (f"Tamanho da Estrutura: {registroSinasc.size}")

    #Pegando o tamanho do arquivo e divindo pelo tamanho de cada registro para saber a qtd de registros
    n = tamanho // registroSinasc.size
    print( f"Quantidade de registros: {n}")

    #Busca Sequencial
    contador = 0
    contador2 = 0
    fcontador = n
    procurado = "355030"
    f.seek(0)
    while contador < fcontador :
        contador += 1
        line = f.read(structlength)
        if len(line) == structlength:
            registro = registroSinasc.unpack(line)
            codmunnasc = registro[0].decode()
        if codmunnasc == procurado:
            file_exists = os.path.isfile("sinasc-sp-capital-2018.dat") 
            if file_exists:
                with open ("sinasc-sp-capital-2018.dat","a+") as f1:
                    f1.write(f"{line}\n")
                    contador2 += 1
            else:
                with open ("sinasc-sp-capital-2018.dat","w+") as f2:
                    f2.write(f"{line}\n")
                    contador2 += 1
    print(f"{contador2}")
