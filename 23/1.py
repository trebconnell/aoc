numbers = [[f"{d}", f"{d}"] for d in range(10)] + list(
    zip(
        [
            "zero",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ],
        [f"{d}" for d in range(10)],
    )
)

sum = 0
with open("1_input.txt") as f:
    for line in f.readlines():
        f_d = ""
        f_i = 100000000000000
        b_d = ""
        b_i = -2
        for s, d in numbers:
            line = line.lower()
            i = line.find(s)
            if i == -1:
                continue

            if i < f_i:
                f_d = d
                f_i = i
            i = line.rfind(s)
            if i > b_i:
                b_d = d
                b_i = i
        sum += int(f_d + b_d)
print(sum)
