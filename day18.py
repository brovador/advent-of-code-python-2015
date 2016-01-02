#encoding: utf-8
import sys
import os
import re

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [l.strip() for l in f]

    lights = [list(c) for c in commands]
    size = len(lights)
    OFF = '.'
    ON = '#'

    def compute_light(x, y, lights):
        result = OFF
        light = lights[x][y]
        neighbours = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i in range(size) and j in range(size) and (i,j) != (x,y):
                    neighbours.append(lights[i][j])
        if light == ON:
            result = ON if neighbours.count(ON) in [2,3] else OFF
        elif light == OFF:
            result = ON if neighbours.count(ON) == 3 else OFF
        return result


    def print_lights(lights):
        print '\n'.join([''.join(l) for l in lights])


    def lights_iterator(lights):
        old_lights = lights
        while True:
            new_lights = [[OFF] * size for x in range(size)]

            old_lights[0][0] = ON
            old_lights[0][size - 1] = ON
            old_lights[size - 1][0] = ON
            old_lights[size - 1][size - 1] = ON

            for x in range(size):
                for y in range(size):
                    new_lights[x][y] = compute_light(x, y, old_lights)

            new_lights[0][0] = ON
            new_lights[0][size - 1] = ON
            new_lights[size - 1][0] = ON
            new_lights[size - 1][size - 1] = ON

            yield new_lights
            old_lights = new_lights



    next_lights = lights
    #print_lights(lights)
    it = lights_iterator(lights)
    for i in range(100):
        print 'After {0} step:'.format(i + 1)
        next_lights = it.next()
        #print_lights(next_lights)
    print sum([x.count(ON) for x in next_lights])






if __name__ == '__main__':
    main()
