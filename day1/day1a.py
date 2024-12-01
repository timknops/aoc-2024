with open("input.txt", "r") as f:
    data = [tuple(map(int, line.split())) for line in f]

list1, list2 = zip(*data)
list1, list2 = sorted(list1), sorted(list2)

print(sum(abs(list1[i] - list2[i]) for i in range(len(list1))))

