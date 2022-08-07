# # Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def solution(x):
    string = str(x)
    
    if string[0] == '-':
        return int('-'+string[:0:-1])
    else:
        return int(string[::-1])
    
print(solution(-231))
print(solution(345))


def solution(A):
    positive_set = set()
    for i in A:
       If i > 0:
        positive_set.add(i)
        
    positive_A = list (positive_set)
    positive_A.sort()
    
    missing_int =1
    for i in positive_A
        if missing_int < i:
            break
        else   
            missing_int += 1
    return missing_int

