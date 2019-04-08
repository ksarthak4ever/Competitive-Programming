'''Given an array of integers, every element appears twice except for one.
Find that single one.''' 

nums = [1,1,2,2,3,1,2,2]
ans = 0

for i in range(len(nums)):
	ans ^= nums[i]