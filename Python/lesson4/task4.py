arr = list(map(int, input().split()))
lef = int(input())
rig = int(input())
if lef >= 0 or rig >= 0:
    arr_1 = arr[lef:rig: -1]
    arr_1.sort(reverse=True)
    print(arr_1)
elif lef <= -1 or rig <= -1:
    arr_1 = arr[rig:lef: -1]
    arr_1.sort(reverse=True)
    print(arr_1)                       #Сломал мозг!!!
elif lef <= -1 or rig >= 0:            #Выводит не то что надо
    arr_1 = arr[lef:rig: -1]           #Пробывал индексы через кортеж,тоже какая то ерунда
    arr_1.sort(reverse=True)           
    print(arr_1)                       #ПАМАГИТИ!!!!)
elif lef >= 0 or rig <= -1:
    arr_1 = arr[lef:rig: -1]
    arr_1.sort(reverse=True)
    print(arr_1)
    


