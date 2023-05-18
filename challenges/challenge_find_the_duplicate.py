def find_duplicate(nums):
    if nums is None:
        return False

    nums.sort()

    for index in range(1, len(nums)):
        if type(nums[index]) != int or nums[index] < 1:
            return False
        if nums[index] == nums[index - 1]:
            return nums[index]
    return False
