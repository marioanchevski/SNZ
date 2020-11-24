def resenie2(l,k):
    k=k%len(l) # primer ako k e 5 a listata ima 3 elementi
    l = l[k:] +l[:k]
    print(l)

if __name__ == '__main__':
    l = list(map(int, input().split(' ')))
    k = int(input())
    resenie2(l,k)

