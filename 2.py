# درج کردن در آرایه نامرتب )می دانیم آخرین خانه خالی می باشد( 
# O(1) -2

def insert_unsorted(arr, element):
    arr[len(arr) - 1] = element

my_array = [1, 3, 5, 7, None]
insert_unsorted(my_array, 9)
print(my_array)