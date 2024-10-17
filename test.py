nums = [1,1,2,4,4,4,4,5,5,5,6,7]

visited = []
for idx, val in enumerate(nums):
    if val not in visited:
        visited.append(val)
    else:
        del nums[idx]

print(nums)