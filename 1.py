# درج در یک آرایه مرتب
# O(N)
def insert_sorted(arr, element):
    index = 0
    while index < len(arr) and arr[index] < element:
        index += 1
    arr.insert(index, element)

my_array = [1, 3, 5, 7, 9]
insert_sorted(my_array, 4)
print(my_array)