word = input()
print(range(len(word) // 10))
for i in range(len(word)//10):
    print(word[i*10-10:i*10])