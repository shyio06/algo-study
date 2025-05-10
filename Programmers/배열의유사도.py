def solution(s1,s2):
    int(count) = 0
    for i in range(len(s1)):
        if s2.count(s1[i]) > 1:
            count +=1
    return count


def solution(s1,s2):
    int(count) = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                count += 1
    return count


def solution(s1, s2):
    int(count) = 0
    for i in s1:
        if i in s2 :
            count += 1
    return count


def solution(s1, s2):
    int(count) = 0
    for i in range(len(s1)):
        if s1[i] in s2 :
            count += 1
    return count