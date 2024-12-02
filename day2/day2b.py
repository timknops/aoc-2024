from collections import Counter

with open("input.txt", "r") as f:
    data = [list(map(int, line.split())) for line in f]

def is_safe_report(arr):
    is_decreasing = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
    is_increasing = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    valid_differences = all(abs(arr[i] - arr[i + 1]) <= 3 for i in range(len(arr) - 1))
    return (is_decreasing or is_increasing) and valid_differences

def safe_by_removing_one_el(arr):
    for i, _ in enumerate(arr):
        if is_safe_report(arr[:i] + arr[i + 1:]):
            return True

    return False

filtered_data = []
for el in data:
    duplicates = [num for num, count in Counter(el).items() if count > 1]

    if duplicates:
        if len(duplicates) == 1 and duplicates[0] in el:
            el.remove(duplicates[0])
            filtered_data.append((True, el))
    else:
        filtered_data.append((False, el))

valid_data = []
for is_modified, el in filtered_data:
    if (is_modified and is_safe_report(el)) or (not is_modified and (is_safe_report(el) or safe_by_removing_one_el(el))):
        valid_data.append(el)

print(len(valid_data))