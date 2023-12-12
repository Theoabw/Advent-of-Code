nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
}

nums_list = list(nums.values()) + list(nums.keys())

with open("../inputs/1") as raw:
    txt_input = [line for line in raw.read().split("\n") if line]


def part1(list_input):
    for i, line in enumerate(list_input):
        ns = ""
        for char in line:
            if char.isdigit():
                ns += char
        ns = ns[0] + ns[-1]
        list_input[i] = int(ns)

    return sum(list_input)


def starts_checker(item: str) -> bool:
    for number in nums_list:
        if item.startswith(number):
            return True
    return False


def ends_checker(item: str) -> bool:
    for number in nums_list:
        if item.endswith(number):
            return True
    return False


def part2(list_input):
    for i, line in enumerate(list_input):
        ns = ""
        while not starts_checker(line):
            line = line[1:]
        while not ends_checker(line):
            line = line[:-1]

        if line[0].isdigit():
            ns += line[0]
        else:
            for num in list(nums.keys()):
                if line.startswith(num):
                    ns += nums[num]

        if line[-1].isdigit():
            ns += line[-1]
        else:
            for num in list(nums.keys()):
                if line.endswith(num):
                    ns += nums[num]

        list_input[i] = int(ns)

    return sum(list_input)


print(f"part 1: {part1(txt_input.copy())}")
print(f"part 2: {part2(txt_input.copy())}")
