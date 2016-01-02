#encoding: utf-8
import sys
import os
import re

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [l.strip() for l in f]


    wires = {}
    for c in commands:
        m = re.match(r'([\w ]+) -> ([\w ]+)', c)
        wires[m.groups()[1]] = m.groups()[0]
    wires['b'] = '956'

    def is_wire(x):
        result = re.match('[a-z]', x)
        return result


    def process_assign(v):
        return int(v)

    def process_operator(x, operator, y):
        x = int(x) if not is_wire(x) else process_wire(x)
        y = int(y) if not is_wire(y) else process_wire(y)

        result = 0
        if operator == 'AND':
            result = x & y
        elif operator == 'LSHIFT':
            result = x << y
        elif operator == 'RSHIFT':
            result = x >> y
        elif operator == 'OR':
            result = x | y
        return result

    def process_switch(x):
        x = int(x) if not is_wire(x) else process_wire(x)
        return ~x


    def process_wire(x):
        v = wires[x]
        for e,f in exprs:
            m = re.match(e, v)
            if m:
                result = f(*m.groups())
                wires[x] = str(result)
                return result

    exprs = [
        ('(\w+) (AND|LSHIFT|RSHIFT|OR) (\w+)', process_operator),
        ('NOT (\w+)', process_switch),
        ('(\d+)', process_assign),
        ('([a-z]+)', process_wire),
    ]

    print process_wire('a') & 0xFFFF

if __name__ == '__main__':
    main()
