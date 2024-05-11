# یافتن کوچکترین عنصر در آرایه مرتب
# O(1)

def find_min_element(arr):
    if len(arr) == 0:
        return None
    return arr[0]

my_array = [1, 3, 5, 7, 9, 11, 13, 15]
min_element = find_min_element(my_array)
print(f"minimum element is : {min_element}")