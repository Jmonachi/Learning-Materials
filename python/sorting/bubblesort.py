def sort(nums):
    for x in range(len(nums)-1, 0, -1):
    	for y in range(x):
    		if nums[y] > nums[y + 1]:
    			temp = nums[y]
    			nums[y] = nums[y + 1]
    			nums[y + 1] = temp


nums = [5,3,8,6,7,2]

sort(nums)

print(nums)