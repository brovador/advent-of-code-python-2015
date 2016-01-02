#encoding: utf-8
import sys
import os
import re
import string

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [l.strip() for l in f if l.strip() != '']

    times = {}
    def find_divisors(num):
        result = set([])
        for x in range(1, int(num ** 0.5) + 1):
            if num % x == 0:
                if times.setdefault(x, 0) < 50:
                    result.add(x)
                    times[x] += 1
                if times.setdefault(num / x, 0) < 50:
                    result.add(num / x)
                    times[num / x] += 1
        return result

    def gifts_for_house(num):
        return 11 * sum(find_divisors(num))

    objective = 29000000
    for i in range(objective / 11):
        gi = gifts_for_house(i)
        print i, gi
        if gi > objective:
            break

if __name__ == '__main__':
    main()
