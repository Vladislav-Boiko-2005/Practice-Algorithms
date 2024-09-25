def speedsort(mas):
    if len(mas)<2:return mas
    elem=mas[len(mas)//2]
    chet_elem=0
    small=[]
    big=[]
    for i in mas:
        if i==elem:chet_elem+=1
        if i>elem:big.append(i)
        if i<elem:small.append(i)
    return speedsort(small)+[elem]*chet_elem+speedsort(big)
while True:
    print(speedsort([int(x) for x in input().split()]))
