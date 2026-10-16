def quick_sort(sort_list):
    if len(sort_list) <= 1:
        return sort_list

    if sort_list == []:
        return []

    pivot = sort_list[0]

    mid = [x for x in sort_list if x == pivot]
    left = [x for x in sort_list if x < pivot]
    right = [x for x in sort_list if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)
# quick sorts fairly easy but also memory-intensive