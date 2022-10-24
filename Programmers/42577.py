# 시간 초과 (마지막 2개)
# def solution(phone_book):
#     for i in phone_book:
#         for j in phone_book:
#             if i != j and len(i) < len(j) and i == j[:len(i)]:
#                 return False
#     return True


# 정렬 사용
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

# 해시 사용
def solution(phone_book):
    hash = dict()
    for i in phone_book:
        hash[i] = 1

    for i in phone_book:
        temp = ''
        for j in i:
            temp += j
            if temp in hash and temp != i:
                return False
    return True




print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))