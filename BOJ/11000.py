import heapq

n = int(input())
arr = []
for _ in range(n):
    s, t = map(int, input().split())
    arr.append([s, t])
# arr.sort(key=lambda x: (x[0], x[1]))
# a = arr[0][1]
# next = []
# cnt = 0
# while 1:
#     for i in range(1, len(arr)):
#         if a <= arr[i][0]:
#             a = arr[i][1]
#         else:
#             next.append(arr[i])
#     arr = next
#     cnt += 1
#     if next == []:
#         break
#     next = []
# print(cnt)

arr.sort()
room = []
heapq.heappush(room, arr[0][1])
for i in range(1, n):
    if arr[i][0] < room[0]:
        heapq.heappush(room, arr[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, arr[i][1])
print(len(room))