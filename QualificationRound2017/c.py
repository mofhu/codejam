x = int(input())

for case in range(1, x + 1):
    n, k = [int(s) for s in input().split(" ")]
    # print(nums)
    spaces = [n]
    y = 0
    z = 0
    for i in range(0, k):
        t = spaces[-1]
        # print(t)
        if t is 1:
            del spaces[-1]
            y, z = 0, 0
        elif t % 2 is 0:
            del spaces[-1]
            if t > 2:
                spaces += [int(t/2-1), int(t/2)]
            else:
                spaces += [1]
            y, z = t/2, t/2-1
        else:
            del spaces[-1]
            spaces += [int((t-1)/2), int((t-1)/2)]
            y, z = (t-1)/2, (t-1)/2
        spaces = sorted(spaces)
        # print(spaces, y, z)

    print("Case #{}: {} {}".format(case, int(y), int(z)))

