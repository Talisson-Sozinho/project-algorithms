def sort_num_list(num_list, start=0, end=None):
    if end is None:
        end = len(num_list)

    if (end - start) == 1:
        if (
            num_list is None
            or type(num_list[start:end][0]) != int
            or num_list[start:end][0] < 1
        ):
            raise ValueError

    if (end - start) > 1:
        mid = (start + end) // 2
        sort_num_list(num_list, start, mid)
        sort_num_list(num_list, mid, end)
        merge_sort(num_list, start, mid, end)


def merge_sort(num_list, start, mid, end):
    left = num_list[start:mid]
    right = num_list[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            num_list[general_index] = right[right_index]
            right_index = right_index + 1

        elif right_index >= len(right):
            num_list[general_index] = left[left_index]
            left_index = left_index + 1

        elif left[left_index] < right[right_index]:
            num_list[general_index] = left[left_index]
            left_index = left_index + 1

        else:
            num_list[general_index] = right[right_index]
            right_index = right_index + 1


def find_duplicate(nums):
    try:
        sort_num_list(nums)
    except ValueError:
        return False

    for index in range(1, len(nums)):
        if nums[index] == nums[index - 1]:
            return nums[index]
    return False
