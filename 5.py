# یافتن عناصر مشترک بین دو آرایه یکی مرب و دیگری نامرتب
# O(nlogn)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def find_common_elements_sorted(arr1, arr2):
    arr1_sorted = merge_sort(arr1)
    arr2_sorted = merge_sort(arr2)

    common_elements = []
    i = j = 0
    while i < len(arr1_sorted) and j < len(arr2_sorted):
        if arr1_sorted[i] == arr2_sorted[j]:
            common_elements.append(arr1_sorted[i])
            i += 1
            j += 1
        elif arr1_sorted[i] < arr2_sorted[j]:
            i += 1
        else:
            j += 1
    return common_elements

array1 = [1, 3, 5, 7, 9]
array2 = [2, 3, 4, 7, 8]
result = find_common_elements_sorted(array1, array2)
print(result)