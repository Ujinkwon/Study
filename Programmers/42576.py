def solution(participant, completion):
    # answer = ''
    # for c in range(len(completion)):
    #     for p in range(len(participant)):
    #         if completion[c] == participant[p]:
    #             completion[c] = 0
    #             participant[p] = 0

    # for i in participant:
    #     if i != 0:
    #         answer = i
    # return answer

    completion.sort()
    participant.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[-1]
                

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))