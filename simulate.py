
import random


def main():
    results = [0]*15
    for i in range(10000):
        r = roll()
        for x in r:
            results[x] += 1
    print results



def roll():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)

    sums = [d1+d2,d1+d3,d2+d3]
    h = set(sums)
    for s in sums:
        if s >= 10:
            h.add(s+2)
    return h

main()
