def intersection(first_list, second_list):
    overlap_list = []
    if len(first_list) == 0 or len(second_list) == 0:
        overlap_list = []
    else:
        for f in first_list:
            for s in second_list:
                if f == s:
                    overlap_list.append(f)
    return overlap_list

print(intersection([3,4], [1,2,3]))
# => [3]
print(intersection([1,7,2,9,4,-3], [2,43,3,1,-100]))
# => [1,2]
print(intersection([1,2,3,4], [4,3,2,1]))
# => [1,2,3,4]
print(intersection([190,732,23,9,4,-3], [2,43,3,1,-100]))
# => []
print(intersection([], [1,2,3]))
# => []
print(intersection([], []))
# => []