#encoding: utf-8
import sys
import os

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [c for c in f.read().strip()]

    houses = set()
    houses.add((0,0))
    coords = [(0,0), (0,0)]

    for i,c in enumerate(commands):
        new_coords = (0, 0)
        if c == '^':
            new_coords = (0, 1)
        elif c == 'v':
            new_coords = (0, -1)
        elif c == '<':
            new_coords = (-1, 0)
        elif c == '>':
            new_coords = (1, 0)
        coords[i % 2] = tuple(map(sum, zip(coords[i % 2], new_coords)))
        houses.add(coords[i % 2])
    print len(houses)



if __name__ == '__main__':
    main()
