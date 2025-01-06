def solution(array, commands):
    answer = []
    for l in commands:
        i,j,k = l
        answer.append(sorted(array[i-1:j])[k-1])
    return answer