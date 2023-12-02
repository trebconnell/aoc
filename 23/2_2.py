sum = 0
with open("2_input.txt") as f:
    i = 0
    for line in f.readlines():
        i += 1
        offset = len(f"Game {i}:")
        ssss = line[offset:].split(";")
        maxes = {"red": 0, "green": 0, "blue": 0}
        for sss in ssss:
            ss = sss.split(",")
            for s in ss:
                s = s.strip()
                (n, c) = s.split(" ")
                maxes[c] = max(int(n), maxes[c])
        power = 1
        for n in maxes.values():
            power *= n
        sum += power


print(sum)
