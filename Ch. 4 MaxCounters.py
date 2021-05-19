def solution(N, A):
    maximum = 0
    lst = [0]*N
    for x in A:
        if x == N + 1:
            lst = [maximum] * N
        else:
            lst[x-1] +=1
            if lst[x-1] > maximum:
                maximum = lst[x-1]
    return lst
