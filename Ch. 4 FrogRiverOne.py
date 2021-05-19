
#first try, final score: 63 (task score 63%, correctness 100%, performance 20%)
def solution(X, A):
    lst = []
    for i in range(1, X+1):
        lst.append(i)
    for i, x in enumerate(A):
        if x in lst:
            lst.remove(x)
        if len(lst)==0:
            return i
    if len(lst) != 0:
        return -1

#second try, final score: 100
def solution2(X, A):
    dict = {}
    for i in range(len(A)):
        dict[A[i]] = i
        if len(dict) == X:
            return i
    return -1