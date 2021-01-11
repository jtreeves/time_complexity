def is_sorted(input):
    for i in range(len(input) - 1):
        if input[i] > input[i + 1]:
            return False
    return True

def bubble_sort(input):
    while not is_sorted(input):
        for i in range(len(input) - 1):
            if input[i] > input[i + 1]:
                input[i], input[i + 1] = input[i + 1], input[i]
    return input

print(is_sorted([1, 4, 6, 3, 9]))
#  => False
print(bubble_sort([1, 4, 6, 3, 9]))
#  => [1, 3, 4, 6, 9]
print(is_sorted([1, 2, 3, 4, 5]))
#  => True
print(bubble_sort([1, 2, 3, 4, 5]))
#  => [1, 2, 3, 4, 5]