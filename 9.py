# محاسبه مقدار میانگین در یک آرایه دوبعدی mدر n و افزودن مقدار میانگین به سطر اول
# O(m*n)


def calculate_average_2d(array):
    total_sum = 0
    num_elements = 0

    for row in array:
        for element in row:
            total_sum += element
            num_elements += 1
    
    average = total_sum / num_elements
    
    array[0].append(average)

    return array

my_2d_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

my_2d_array_with_avg = calculate_average_2d(my_2d_array)
for row in my_2d_array_with_avg:
    print(row)