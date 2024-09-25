def binp (mas,item):
    mas=sorted(mas)
    begin=0
    end=len(mas)-1
    while (begin<=end):
        sred=(begin+end)//2
        if item==mas[sred]:return sred
        if item>mas[sred]:begin=sred+1
        if item<mas[sred]:end=sred-1
    return -1
while True:
    n=int(input())
    mas=[int(x) for x in input().split()]
    print(binp(mas,n)) 