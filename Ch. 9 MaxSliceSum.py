def solution(A):
    m = A[0] #maximum of the sums is set to the first value by default (subjected to change later on)
    s = 0 #the sum at hand
    for i in A:
        s += i #add each value to the sum variable
        if s > m: #if sum is greater than maximum,
            m = s #set the maximum variable to the sum
        if s < 0: #if sum is less than 0, there's no way it is the maximum sum value
            s = 0 #so reset the value of sum
    return m
