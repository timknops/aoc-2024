with open("input.txt", "r") as f:
    data = [tuple(map(int, line.split())) for line in f]

list_1, list_2 = zip(*data)
list_1, list_2 = sorted(list_1), sorted(list_2)

print(sum(abs(list_1[i] - list_2[i]) for i in range(len(list_1))))

