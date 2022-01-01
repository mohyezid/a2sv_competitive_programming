output=[]
nums=[0,1,0,3,12]
for i in range(len(nums)):
    if nums[i]==0:
        nums.pop(i)
        nums.append(0)

print(nums)
