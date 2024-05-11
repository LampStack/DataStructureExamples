# یافتن کوچکترین عنصر در آرایه نامرتب
# O(n)

def find_min_element_unsorted(arr):
    if len(arr) == 0:
        return None
    min_element = arr[0]
    for element in arr:
        if element < min_element:
            min_element = element
    return min_element

my_array = [9, 3, 5, 7, 1, 11, 13, 15]
min_element = find_min_element_unsorted(my_array)
print(f"minimum element is : {min_element}")