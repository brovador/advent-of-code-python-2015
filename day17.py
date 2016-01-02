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

    data = [int(x) for x in commands]
    n = 0
    minimun = 10000
    liters = 150
    for i in range(len(data)):
        combs = itertools.combinations(data, i)
        while True:
            try:
                c = combs.next()
                if sum(c) == liters  and len(c) <= minimun:
                    if len(c) < minimun:
                        minimun = len(c)
                        n = 1
                    else:
                        n += 1
            except:
                break
    print n



if __name__ == '__main__':
    main()
