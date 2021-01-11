def two_sum1(number_list, sum):
    for i in range(len(number_list)):
        for j in range(len(number_list)):
            if (i != j) and (number_list[i] + number_list[j] == sum):
                return [i, j]

# QUADRATIC TIME COMPLEXITY

print(two_sum1([11, 2, 7, 15], 9))
# => [1,2]
print(two_sum1([3, 2, 9, 11], 5))
# => [0,1]
print(two_sum1([17, 8, 22, 1, 4, 6], 5))
# => [3,4]
print(two_sum1([1, 8, 22, 3, 4, 5], 4))
# => [0,3]
print(two_sum1([1, 2, 3, 4, 5, 6], 40))
# => None

# ALTERNATIVE ---------------------------------------------------

# PROBLEM: This does not work because dictionary does not have property has_key (may be a Python 2 thing, as it came from Pete)

def two_sum2(number_list, sum):
    intermediary = {}
    for i in range(len(number_list)):
        diff = str(sum - number_list[i])
        intermediary[diff] = i
    for j in range(len(number_list)):
        value = str(number_list[j])
        if intermediary.has_key(value) and j != intermediary[value]:
            return [j, intermediary[value]]

# LINEAR TIME COMPLEXITY

print(two_sum2([11, 2, 7, 15], 9))
# => [1,2]
print(two_sum2([3, 2, 9, 11], 5))
# => [0,1]
print(two_sum2([17, 8, 22, 1, 4, 6], 5))
# => [3,4]
print(two_sum2([1, 8, 22, 3, 4, 5], 4))
# => [0,3]
print(two_sum2([1, 2, 3, 4, 5, 6], 40))
# => []