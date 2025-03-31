def find(search_list, value):
    left, right = 0, len(search_list) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    raise ValueError("value not in array")
