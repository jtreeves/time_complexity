def intersection1(first_list, second_list):
    overlap_list = []
    if len(first_list) == 0 or len(second_list) == 0:
        overlap_list = []
    else:
        for f in first_list:
            for s in second_list:
                if f == s:
                    overlap_list.append(f)
    return overlap_list

# QUADRATIC TIME COMLPEXITY
# nested for loops (linear * linear = quadratic)
# less ideal

print(intersection1([3,4], [1,2,3]))
# => [3]
print(intersection1([1,7,2,9,4,-3], [2,43,3,1,-100]))
# => [1,2]
print(intersection1([1,2,3,4], [4,3,2,1]))
# => [1,2,3,4]
print(intersection1([190,732,23,9,4,-3], [2,43,3,1,-100]))
# => []
print(intersection1([], [1,2,3]))
# => []
print(intersection1([], []))
# => []

# ALTERNATIVE APPROACH ------------------------------------------

def intersection2(first_list, second_list):
    overlap_list = []
    intermediary_dictionary = {}
    if len(first_list) == 0 or len(second_list) == 0:
        overlap_list = []
    else:
        for f in first_list:
            intermediary_dictionary[str(f)] = True
        for s in second_list:
            if str(s) in intermediary_dictionary:
                overlap_list.append(s)
    return overlap_list

# LINEAR TIME COMPLEXITY
# parallel for loops (linear + linear = still linear)
# more ideal

print(intersection2([3,4], [1,2,3]))
# => [3]
print(intersection2([1,7,2,9,4,-3], [2,43,3,1,-100]))
# => [1,2]
print(intersection2([1,2,3,4], [4,3,2,1]))
# => [1,2,3,4]
print(intersection2([190,732,23,9,4,-3], [2,43,3,1,-100]))
# => []
print(intersection2([], [1,2,3]))
# => []
print(intersection2([], []))
# => []