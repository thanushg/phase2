nums =[12,13,4,99,34]
target=0
nums=sorted(nums)
left=0
right=len(nums)-1
flag=-1

while left <=right:
    mid = (left + right) // 2
    if nums[mid]==target:
        flag = mid
        break
    elif nums[mid]>target:
        right = mid -1
    else:
        left = mid +1
if flag ==-1:
    print("Target Not Found")
else:
    print("Target found at index:",flag)