alpa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
l = 'abcdefghijklmnopqrstuvwxyz'

char = input()
cnt = 0
result = char

for i in alpa:
    if i in result:
        cnt += result.count(i)
        result = result.replace(i, ' ')

print(cnt+len(result.replace(' ','')))
