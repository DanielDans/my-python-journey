def merge_sort(arr): # base function
    if len(arr) <= 1: # base case checking if it has already split to 1
        return arr # sends arr as an output

    mid = len(arr) // 2 # interpretation of the middle
    min = merge_sort(arr[:mid]) # recursive call to the left side of array, splits it into halves until base case
    max = merge_sort(arr[mid:]) # recursive call to the right side of array, splits it into halves until base case

    sorted = []
    i = 0 # base pointer for left
    j = 0 # base pointer for right

    while i < len(min) and j < len(max): # while loop to check if the left and right side of the array is less than the length of the array
        if min[i] < max[j]: # if the left side is less than the right
            sorted.append(min[i]) # append left to sorted array
            i += 1 # looks at next element in the left
        else: # if the right side is less than the left
            sorted.append(max[j]) # append right to sorted array
            j += 1 # looks at next element in the right

    sorted.extend(min[i:]) # extend sorted array with remaining elements in the left
    sorted.extend(max[j:]) # extend sorted array with remaining elements in the right

    return sorted

them = [8, 7, 4, 3, 9, 2, 0, 1] # array to be sorted
print("Unsorted array:", them) # prints the unsorted array
sorted_array = merge_sort(them)
print("Sorted array:", sorted_array) # prints the sorted array

# freecodecamp

def binary_search(search_list, value):
    path_to_target = []
    low = 0
    high = len(search_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)
        
        if value == value_at_middle:
            return path_to_target, f'Value found at index {mid}'
        elif value > value_at_middle:
            low = mid + 1
        else:
            high = mid - 1
    
    return [], "Value not found"

print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))
print(binary_search([1, 3, 5, 9, 14, 22], 10))