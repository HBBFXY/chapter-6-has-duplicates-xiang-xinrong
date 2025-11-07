def has_duplicates(lst):
    return len(lst) != len(set(lst))

test_cases = [[1,2,3,4], [1,2,2,3], [], [5]]
for case in test_cases:
    print(has_duplicates(case))
