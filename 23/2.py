sum = 0
min = {"red": 12, "green": 13, "blue": 14}
with open("2_input.txt") as f:
    i = 0
    for line in f.readlines():
        i += 1
        offset = len(f"Game {i}:")
        ssss = line[offset:].split(";")
        bad = False
        for sss in ssss:
            ss = sss.split(",")
            counts = {"green": 0, "red": 0, "blue": 0}
            for s in ss:
                s = s.strip()
                (n, c) = s.split(" ")
                counts[c] += int(n)
            for c, n in counts.items():
                if n > min[c]:
                    bad = True
                    break
            if bad:
                break
        assert len(counts) == 3
        if not bad:
            sum += i

print(sum)
