def pre_process(pattern):
    m = len(pattern)   # 패턴의 길이
    
    skip_table = dict()
    for i in range(m-1):
        skip_table[pattern[i]] = m - i - 1

    return skip_table


def boyer_moore(text, pattern):
    skip_table = pre_process(pattern)
    m = len(pattern)
    i = 0   # text idx

    while i <= len(text) - m:
        j = m - 1    # 뒤에서 비교
        k = i + (m - 1)  # 비교 시작 idx
        # 비교할 j가 남아있고, text와 pattern이 일치하면 그 다음 앞 글자 비교를 위해 인덱스 감소
        while j >= 0 and pattern[j] == text[k]:
            j -= 1
            k -= 1
        if j == -1:   # 일치
            return i
        
        # 일치X
        else:
            # i 비교할 시작 위치를 skip table에서 가져옴
            i += skip_table.get(text[i+m-1], m)
    return -1   # 일치 패턴 X
    

text = 'ABC ABCDAB ABCDABCDABDE'
pattern = 'ABCDABD'
print(boyer_moore(text, pattern))

