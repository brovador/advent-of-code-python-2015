#encoding: utf-8
import sys
import os
import re
import itertools
from operator import mul

def main():
    global min_mana_spent

    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [x for x in f]
    
    serie = (1,0)
    last_value = 20151125
    result = (2978, 3083)

    i = 0
    while True:
        row, col = (serie[0] - serie[1]), serie[1] + 1
        if (row, col) != (1, 1):
            last_value = (last_value * 252533) % 33554393

        if (row, col) == result:
            print 'codes: {}, {} = {}'.format(row, col, last_value)
            break

        i += 1
        serie = (serie[0], serie[1] + 1)
        if serie[0] == serie[1]:
            serie = (serie[0] + 1, 0)


if __name__ == '__main__':
    main()
