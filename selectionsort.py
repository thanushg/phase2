def performInsertionSort(nums):
    n=len(nums)
    lastEleInSortArr=0
    for firstIndex in range(1,n):
        temp = nums[firstIndex]
        previous = lastEleInSortArr
        while previous>=0 and nums[previous]>temp:
            nums[previous+1]=nums[previous]
            previous=previous-1
        
        nums[previous+1]=temp
        print(nums)
        lastEleInSortArr+=1
    
nums = list(map(int,input().split()))    
print("before sorting :",nums)

performInsertionSort(nums)
print("after sorting :",nums)

