#encoding: utf-8
import sys
import os
import re

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [l.strip() for l in f]

    w, h = 1000, 1000
    lights = [0.0] * w * h

    def process_command(command, c1, c2):
        for i in range(c1[0], c2[0] + 1):
            for j in range(c1[1], c2[1] + 1):
                x = i * w + j
                if command == 'turn on':
                    lights[x] += 1.0
                elif command == 'turn off':
                    lights[x] = max(lights[x] - 1.0, 0.0)
                elif command == 'toggle':
                    lights[x] += 2.0

    r = re.compile('(?P<command>turn on|toggle|turn off) (?P<c1>\d+),(?P<c2>\d+) through (?P<c3>\d+),(?P<c4>\d+)')
    for c in commands:
        m = r.match(c)
        process_command(m.group('command'),
            (int(m.group('c1')), int(m.group('c2'))),
            (int(m.group('c3')), int(m.group('c4'))))

    print sum(lights)

if __name__ == '__main__':
    main()
