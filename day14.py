#encoding: utf-8
import sys
import os
import re

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [l.strip() for l in f]

    r = re.compile(r'(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds.')
    data = {}
    for c in commands:
        n, v, tv, tr = r.match(c).groups()
        data[n] = (int(v), int(tv), int(tr))

    secs = 2503
    scores = {}

    def simulate(sec, data):
        v, tv, tr = data
        n = int(sec / (tv + tr))
        r = sec % (tv + tr)
        d = v * (tv * n + min(r, tv))
        return d

    for i in range(secs):
        best_reindeers = []
        best_distance = 0
        for name, d in data.iteritems():
            x = simulate(i + 1, d)
            if x >= best_distance:
                best_reindeers = best_reindeers + [name] if x == best_distance else [name]
                best_distance = x
        for name in best_reindeers:
            scores[name] = scores.setdefault(name, 0) + 1
    print reduce(lambda x, y: max(x,y), scores.values())



    # best_d = 0
    # for name, v, tv, tr in data:
    #     v, tv, tr = [int(x) for x in v, tv, tr]
    #     n = int(secs / (tv + tr))
    #     r = secs % (tv + tr)
    #     d = v * (tv * n + min(r, tv))
    #     if d > best_d:
    #         best_d = d
    # print best_d






if __name__ == '__main__':
    main()
