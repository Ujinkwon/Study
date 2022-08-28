def solution(n, lost, reserve):
    reserve2 = list(set(reserve) - set(lost))
    lost = list(set(lost) - set(reserve))
    reserve2.sort()
    lost.sort()
    for i in reserve2:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)

    return n-len(lost)

print(solution(5, [1,2,4,5], [2, 3, 4]))
# print(solution(5, [1,2,4], [2, 4, 5]))
# print(solution(5, [1,2,4], [2, 3, 4, 5]))
# print(solution(5, [2,4], [1, 3, 5]))  # 5
# print(solution(5, [2,4], [3, 5]))   # 5
# print(solution(5, [2,4], [1, 3]))   # 5
# print(solution(5, [2,5], [1, 3]))   # 4
# print(solution(5, [2, 4], [3]))    # 4
# print(solution(3, [3], [1]))   # 2
# print(solution(5, [1, 3], [1]))  # 4
# print(solution(7, [2,4,7], [1,3,5]))  # 6

# reserve중에서 lost한 사람 걸러낼때 모든 요소에 참조하려면 deep copy를 사용해야될것 같아요! 그냥 위에 코드처럼 = 을 사용하면 shall copy가 되어서 같은 메모리주소에 저장이 되서 list값이 변하면 copy하는녀석들도 같이 바뀌는걸 확인했네요!
# deep copy를 하면 copy본이 손상되지 않고 모든요소에 대해서 참고되서 완벽하게 reserve중에서 lost한 녀석들을 걸러낼 수 있을거에요! 앞에분이 말해줬던대로 for문에 remove를 쓰면 for문이 망가지기 쉬워서 다른방법이 좋은듯!

# 참고한 테스트 케이스:n = 5, lost = [1, 2, 4, 5], reserve = [2, 3, 4] --> return 값은 3이 나와야함