
import random
import math
import numpy as np
import matplotlib.pyplot as plt


def main():
    results = [0]*15
    for i in range(10000):
        r = roll()
        for x in r:
            results[x] += 1
    results_dec = map(lambda x: math.floor(x*1.0/(i/100))/100.0 , results)
    print results_dec
    
    plt =  make_chart([ (x,y) for x,y in enumerate(results_dec) if x >= 2])
    plt.savefig('machi_koro_rolls.png',bbox_inches= 'tight')


def make_chart(results):
    print results
    data = results
    data.sort(key = lambda x: x[0])
    print data
    X = map(lambda x: x[0] , data)
    y = map(lambda x: x[1] , data)
    y_pos = np.arange(len(X))

    plt.bar(y_pos,y,align = 'center' , alpha = 0.5)
    plt.xticks(y_pos, X)
    plt.ylabel('Probability of being able to make roll')
    plt.title('Machi Koro endgame roll distribution')

#    plt.show()

    return plt

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
