#encoding: utf-8
import sys
import os
import re
import itertools

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [l.strip() for l in f]

    data = {}
    r = re.compile(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)')
    for c in commands:
        p1, m, h, p2 = r.match(c).groups()
        h = int(h) if m == 'gain' else -int(h)
        data.setdefault(p1, {})[p2] = h

    names = data.keys()
    for n in names:
        data[n]['me'] = 0
        data.setdefault('me', {})[n] = 0

    def hapiness(names):
        result = 0
        for i, n in enumerate(names):
            d = data[n]
            result += d[names[(i - 1) % len(names)]]
            result += d[names[(i + 1) % len(names)]]
        return result

    best_happiness = -sys.maxint
    best_result = None
    for x in itertools.permutations(data.keys()):
        h = hapiness(x)
        if h > best_happiness:
            best_happiness = h
            best_result = x
    print best_result
    print best_happiness




if __name__ == '__main__':
    main()
