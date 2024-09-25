def sort_vibor (mas_vvod):
    mas=mas_vvod
    new_mas=[]
    for j in range(len(mas)):
        minh = mas[0]
        index_min = 0
        for i in range(1,len(mas)):
            if mas[i]<minh:
                minh=mas[i]
                index_min=i
        new_mas.append(minh)
        mas.pop(index_min)
    return new_mas
while True :print(sort_vibor([ int(x) for x in input().split()]))