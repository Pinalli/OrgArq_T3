# Mapeamento direto, com 9 bits para tag, 4 bits para linha, 2 bit
# para palavra e 1 bit para selec~ao do byte em uma palavra (cache
# com 16 linhas, 4 palavras por linha).

class Direct:
    data = ['00','01','10','11','00','01','10','11','00','01','10','11','00','01','10','11']
    byte = 0
    tag = ""
    linha = ""

# Lendo o Arquivo onde estao os 8 Bits
file = open("b.txt","r")

# Inicialicao do array do Cache
cache = [None] * 16

# Variaveis hit e miss
hit = 0
miss = 0

# Cada posicao do cache possui a inicializacao da classe Linha
for p in range (0,16):
    cache[p] = Direct()

# Lendo cada valor de cada linha do arquivo
for line in file:

    tag = line[0:9]
    linha = line[9:13]
    dec = int(linha,2)
    palavra = line[13:15]
    byte = line[15:16]

    print("Tag: " + tag),
    print('Linha:',linha)
    print("Palavra: " + palavra),
    print("byte: " + byte)


    if cache[dec].byte == 0 :
        print("Miss:" + str(line))
        miss = miss + 1
        cache[dec].byte = 1
        cache[dec].linha = linha
        cache[dec].tag = tag
    else:
        if cache[dec].tag != tag :
            print("Miss:" + str(line))
            miss = miss + 1
            cache[dec].tag = tag
        else:
            print("Hit:" + str(line))
            hit = hit + 1
print('\nMapeamento Direto 2.b')
print("Total de Hits:" + str(hit))
print("Taxa de hits:" + str(round((float(hit) / (hit+miss))*10000) / 100) + "%")
print("Total de Misses:" + str(miss))
print("Taxa de misses:" + str(round((float(miss) / (hit+miss))*10000) / 100) + "%")
