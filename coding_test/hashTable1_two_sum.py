def two_sum(nums, target):
    memo = {} # dictionary
    for v in nums:
        memo[v] = True
    for v in nums:
        needed_number = target - v
        if v == needed_number:
            continue
        elif needed_number in memo:
            return True
    return False

nums = [2,1,5,7]

result = two_sum(nums, 4)
print(result)