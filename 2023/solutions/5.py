with open("../inputs/5ex") as raw:
    full_input = raw.read().split("\n\n")
    seeds = list(map(int, full_input[0].split(":")[1].strip().split(" ")))
    maps = [[list(map(int, line.split(" "))) for line in item.split("\n")[1:] if line] for item in full_input[1:]]

print(seeds)
print(maps)
convertable = [seeds]

for item in maps:
    curmap = [convertable[-1]]
    for line in item:
        source = list(range(line[1], line[1] + line[2]))
        destination = list(range(line[0], line[0] + line[2]))
        mapping_dict = dict(zip(source, destination))
        linec = [[mapping_dict.get(num, num) for num in curmap[-1]]]
    convertable += linec

        # there's probably a better way of doing this, but I'm lazy

print(convertable)
