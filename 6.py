# جستجو در آرایه مرتب 
# O(logn)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

my_array = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
index = binary_search(my_array, target)
if index != -1:
    print(f"element {target} find in {index} index")
else:
    print("not found")
