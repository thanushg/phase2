nums = [0,12,34,56,67,89]
target = 89
flag = 1
for index in range(len(nums)):
    if nums[index] == target:
        flag = index
        break
if flag == 1:
    print("target not found")
else:
    print("target found at : ",flag)