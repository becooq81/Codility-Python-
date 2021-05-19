def solution(A):
    th = len(A)//2 + 1 #th stands for threshold, the minimum frequency required for a value to be considered a dominator
    d = dict() #a dictionary that will include the values of A as keys
    for i in range(len(A)):
        if A[i] in d.keys(): #if the value is already a key of the dictionary,
            d[A[i]].append(i) #add the index to the list assigned to the key
        else: #otherwise,
            d[A[i]] = [i] #create the key and assign a list that has the value of the index
        if len(d[A[i]]) >= th: #if the key met the minimum frequency
            return i #it's a dominator
    return -1 #if there's no dominator, return -1