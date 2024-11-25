def twoSum(nums, target):
  for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i,j]
res = twoSum([2,7,11,13], 9)
print(res)

def twoSum(nums, target):
  hash_map = {}
  for i, num in enumerate(nums):
    complement = target - num
    if complement in hash_map:
      return [hash_map[complement], i]
    hash_map[num] = i
  return []
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)

