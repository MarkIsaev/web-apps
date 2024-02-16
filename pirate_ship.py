n,m = map(int, input().split())
arr = []
answer = []
for i in range(m):
    s = input().split()
    arr1 = []
    arr1.append(s[0])
    arr1.append(int(s[1]))
    arr1.append(int(s[2]))
    arr1.append(0) # стоимость за кг, далее посчитаем
    arr.append(arr1)
    
# название груза, вес (целое число), стоимость (целое число), стоимость за кг
for i in range(len(arr)):
    arr[i][3] = arr[i][2]/arr[i][1]

arr =sorted(arr,key=lambda x: x[3])
arr.reverse()
i = 0
while (n>0) and (i<m):
    if not(arr[i][1] > n): # случай когда берём полный вес
        n-=arr[i][1]
        arr1 = []
        arr1.append(arr[i][0])
        arr1.append(arr[i][1])
        arr1.append(arr[i][2])
        answer.append(arr1)
    else: # случай когда берём остаток веса
        new_weight = n
        new_price = (new_weight*arr[i][2])/arr[i][1]
        n-=arr[i][1]
        arr1 = []
        arr1.append(arr[i][0])
        arr1.append(new_weight)
        arr1.append(new_price)
        answer.append(arr1)
    i+=1

for i in range(len(answer)):
    print(f"{answer[i][0]} {answer[i][1]:.2f} {answer[i][2]:.2f}")