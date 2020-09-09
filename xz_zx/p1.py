n, k = input().split()
n = int(n)
k = int(k)
res = []
nums = [i for i in range(1, n + 1)]
track = []

def allsort(nums, track):
    if len(track) == len(nums):
        res.append(track[:])
        return

    for i in range(len(nums)):
        if nums[i] in track:
            continue

        track.append(nums[i])

        allsort(nums, track)

        track.pop(-1)

allsort(nums, track)

RES = []
for i in range(len(res)):
    count = 1
    for j in range(n - 1): # [0, n-2]
        # print(res[0], res[i][j])
        if res[i][j] < res[i][j + 1]:
            count = count + 1

        if count == k:
            RES.append(res[i])

for j in range(len(RES[0])):
    print(RES[0][j], end=" ")




