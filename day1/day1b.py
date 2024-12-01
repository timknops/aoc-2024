from collections import Counter

with open("input.txt", "r") as f:
    data = [tuple(map(int, line.split())) for line in f]

list1, list2 = zip(*data)
list1, list2 = sorted(list1), list2

freq_counter = Counter(list2)

total = sum([num * freq_counter[num] for num in list1])

print(total)
