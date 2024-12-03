import re

with open("input.txt", "r") as f:
    data = f.read()

matches = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", data)

valid_matches, total, included = [], 0, True
for i in range(len(matches)):
    match (matches[i]):
        case "do()":
            included = True
        case "don't()":
            included = False
        case _:
            if not included: continue

            nums = re.findall(r"\d+", matches[i])
            total += int(nums[0]) * int(nums[1])

print(total)

