#encoding: utf-8
import sys
import os
import string
import re
import json

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [l.strip() for l in f]

    data = commands[0]
    data = json.loads(data)

    def clean(d):
        if type(d) == dict:
            return clean_dict(d)
        elif type(d) == list:
            return [clean(x) for x in d]
        else:
            return d

    def clean_dict(d):
        result = {}
        if valid_dict(d):
            result = d
            for k, v in d.iteritems():
                d[k] = clean(v)
        return result
    
    def valid_dict(d):
        return 'red' not in d.values()


    data = clean(data)
    data = json.dumps(data)
    result = sum([int(x.groups()[0]) for x in re.finditer(r'(-?\d+)', data)])
    print result








if __name__ == '__main__':
    main()
