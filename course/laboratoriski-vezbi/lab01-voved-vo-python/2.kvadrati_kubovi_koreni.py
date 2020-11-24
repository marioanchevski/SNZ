import math
if __name__ == "__main__":
    m = int(input())
    n = int(input())
    x = int(input())

    #popolni recnik
    recnik = dict()
    for i in range(m,n+1):
        stepen = i * i
        kub = i*i*i
        koren = math.sqrt(i)
        recnik[i]=(stepen,kub,koren)

    recnik_keys = recnik.keys()
    if x not in recnik_keys:
        print("nema podatoci")
    else:
        print(recnik[x])
    print(recnik)

