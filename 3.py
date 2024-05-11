# یافتن عناصر مشترک بین دو آرایه نامرتب 
# O(n*m)
def find_common_elements(arr1, arr2):
    common_elements = []
    for element in arr1:
        if element in arr2: # have a for with len(arr2)
            common_elements.append(element)
    return common_elements

array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]
result = find_common_elements(array1, array2)
print(result)
