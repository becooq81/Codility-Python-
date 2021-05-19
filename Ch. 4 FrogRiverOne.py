#check whether the list is made of consecutive values


#first try, final score: 63 (task score 63%, correctness 100%, performance 20%)
def solution(X, A):
    lst = []
    for i in range(1, X+1): #make a list that includes all the values from 1 to X
        lst.append(i)
    for i, x in enumerate(A): #as you go through the list A,
        if x in lst: #remove the value of list A that is in lst
            lst.remove(x)
        if len(lst)==0: #if there are no values left in lst,
            return i #return the index at which it happens
    if len(lst) != 0: #if the requirement is never met,
        return -1 #return -1

#second try, final score: 100
def solution2(X, A):
    dict = {}
    for i in range(len(A)): #make a dictionary that has the numbers as keys
        dict[A[i]] = i
        if len(dict) == X: #if the number of keys match X,
            return i #return the moment it happens
    return -1