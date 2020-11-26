
# Mapeamento associativo, com 12 bits para tag, 3 bits para palavra
# e 1 bit para seleçao do byte em uma palavra (cache com 8 linhas,
# 8 palavras por linha)
#



class Associative:
    word = ['000', '001', '010', '011']
    byte = 0
    tag = ""
    word = ""
    count = -1  # contador para mudar posição


# Reading file
file = open("b.txt", "r")

cache = [None] * 16

# Variaveis hit e miss
hit = 0
miss = 0

# Start cache
for p in range(0, 16):
    cache[p] = Associative()

# Counter to walk on the Cache
cacheCount = 0

# to check if cache memory is full
isFull = 16

# to insert the min value of count inside Linha
minValue = -1
# Reading the binary file

for line in file:

    tag = line[0:12]
    word = line[12:15]
    byte = line[15:16]
    print("Tag: " + tag),
    print("Palavra: " + word),
    print("Byte: " + byte)

    if cacheCount != isFull:
        cache[cacheCount].word = line
        cache[cacheCount].tag = tag
        print("Miss;" + str(cache[cacheCount].word))
        miss += 1
        cacheCount += 1
    else:
        if cacheCount == isFull:
            cacheCount = 0
            if cache[cacheCount].tag == tag:
                print("Hit:" + str(cache[cacheCount].word))
                print("Hit Counter: " + str(cache[cacheCount].count))
                hit += 1
                cache[cacheCount].count += 1
            if minValue > cache[cacheCount].count:
                minValue = cache[cacheCount].count
                cacheCount += 1

            if cache[cacheCount].count < minValue:
                cache[cacheCount].tag = tag
                cache[cacheCount].word = word
                cache[cache].count = -1
                print("Miss;" + str(cache[cacheCount].word))
                miss += 1

print('\nMap associativo 2.C')
print("Total de Hits:" + str(hit))
print("Taxa de Hits:" + str(round((float(hit) / (hit + miss)) * 10000) / 100) + "%")
print("Total de Misses:" + str(miss))
print("Taxa de Misses:" + str(round((float(miss) / (hit + miss)) * 10000) / 100) + "%")