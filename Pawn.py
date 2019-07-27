def solution(A):
    jumps = 0
    i = 0
    while 1: 
        if i < 0 or i >= len(A):
            return jumps
        elif A[i] == 0:
            return -1
        jumps += 1
        next = i + A[i]
        A[i] = 0
        i = next
        #print(A)

print(solution([1, 1, -1, 1])) #-1
print(solution([2, 3, -1, 1, 3])) #4
print(solution([2, 3, -1, 1, -5])) #4
print(solution([5, 1, 2, -1, 10, 1, 2, -2])) #3
print(solution([5, 1, 2, -1, 10, 1, -6, -2])) #-1
print(solution([5, 1, 2, -1, 10, 1, -5, -2])) #6