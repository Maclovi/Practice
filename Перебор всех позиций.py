n, m = map(int, input().split())

matrix = [[i for i in input()] for i in range(n)]
cnt = 0
flag = False
for i in range(n):
    for j in range(m):
        if matrix[i][j] == '.':
            for i1 in range(i - (i % n > 0), (i+1) + ((i+1) % n > 0)):    # Установил границы рядов, тем самым не выйдет за диапазон индексов
                for j1 in range(j - (j % m > 0) + (i1 != i), j+1 + ((j+1) % m > 0), 2):    # Установил границы столбцов, тем самым не выйдет за диапазон
                    if matrix[i1][j1] == '*':                                              # границ, также добавил тут условие пербора в 2 шага и зависомость от ряда
                        flag = True
                        break
            else:
                if flag:
                    flag = False
                else:
                    cnt += 1
                        
                            
print(cnt)   
