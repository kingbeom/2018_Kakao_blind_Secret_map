def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        sol=''
        x = bin(arr1[i])
        y = bin(arr2[i])
        x = x[2:]
        y = y[2:]
        if len(x) != n:
            x=('0'*(n-len(x)))+x
        if len(y) != n:
            y=('0'*(n-len(y)))+y
        for j in range(n):
            if x[j]==y[j]:
                if x[j]=='1' and y[j]=='1':
                    sol+='#'
                    continue
                elif x[j]=='0' and y[j]=='0':
                    sol+=' '
                    continue
            sol+='#'
        answer.append(sol)
    return answer

print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))