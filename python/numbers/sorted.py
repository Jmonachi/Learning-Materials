def my_sort(my_list):
    even = [p for p in my_list if p % 2 == 0]
    odd  = [p for p in my_list if p % 2 != 0]
    return sorted(odd) + sorted(even)

my_list = [1,2,3,4,5]

print(my_sort(my_list))


