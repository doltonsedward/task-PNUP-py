def bubleSort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    
    print(list)

list1 = [13, 15, 30, 41, 45, 55, 75, 95, 102, 135, 139, 151, 193, 200]
bubleSort(list1)