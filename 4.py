# یافتن عناصر مشترک بین دو آرایه مرتب
# O(2n) | O(n + m)

def find_common_elements_sorted(arr1, arr2):
    common_elements = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            common_elements.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return common_elements

array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]
result = find_common_elements_sorted(array1, array2)
print(result)
