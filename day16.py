#encoding: utf-8
import sys
import os
import re
import operator

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [l.strip() for l in f]

    data = {}
    r = re.compile(r'Sue (\d+): (.+)')
    r2 = re.compile(r'(\w+): (\d+)')
    for c in commands:
        n, props = r.match(c).groups()
        props = props.split(', ')
        props = [r2.match(p).groups() for p in props]
        props = [(p[0], int(p[1]), ) for p in props]
        props = dict(props)
        data[int(n)] = props

    clue = {
        'children' : 3,
        'cats' : 7,
        'samoyeds' : 2,
        'pomeranians' : 3,
        'akitas' : 0,
        'vizslas' : 0,
        'goldfish' : 5,
        'trees' : 3,
        'cars' : 2,
        'perfumes' : 1,
    }

    def calculate(d):
        score = 0
        for k, v in clue.iteritems():
            if k in d:
                if k in ['cats', 'trees']:
                    score += 100 if d[k] > v else -1000000
                elif k in ['pomeranians', 'goldfish']:
                    score += 100 if d[k] < v else -1000000
                else:
                    score += 100 if d[k] == v else -10000000
            else:
                score += 10
        return score

    best_result = 0
    best_n = -1
    for n, props in data.iteritems():
        c = calculate(props)
        if c > best_result:
            best_result = c
            best_n = n
    print best_n





if __name__ == '__main__':
    main()
