#encoding: utf-8
import sys
import os
import re

best_distance = 0
best_route = None

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [l.strip() for l in f]

    cities = set([])
    distances = {}
    r = re.compile(r'(\w+) to (\w+) = (\d+)')
    for c in commands:
        m = r.match(c)
        c1, c2, d = m.groups()
        distances.setdefault(c1, {})[c2] = int(d)
        distances.setdefault(c2, {})[c1] = int(d)
        cities.add(c1)
        cities.add(c2)

    # 1. Start with each city
    # 2. From a city, pick the next one with the shortest distance
    # 3. Go to 2 and continue until:
    #  3.1 Accumulated distance is bigger than the best solution
    #  3.2 All the cities has been passed
    # 4. If all the cities has been passed y accumulated solution is better
    #  update accumulated solution and path
    # 5. Go to 1



    def next_city(current_route, current_distance):
        global best_distance
        global best_route
        candidates = [c for c in cities if c not in current_route]
        if len(candidates) == 0 and current_distance > best_distance:
            best_distance = current_distance
            best_route = current_route
        else:
            c1 = current_route[-1]
            for c2 in candidates:
                d = distances[c1][c2]
                next_city(current_route + [c2], current_distance + d)

    for c in cities:
        next_city([c], 0)

    print best_distance
    print best_route










if __name__ == '__main__':
    main()
