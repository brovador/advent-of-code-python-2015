#encoding: utf-8
import sys
import os
import re
import string
from operator import add
import itertools

def main():
    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [l.strip() for l in f if l.strip() != '']

    item_shop_raw = '''
        Weapons:    Cost  Damage  Armor
        Dagger        8     4       0
        Shortsword   10     5       0
        Warhammer    25     6       0
        Longsword    40     7       0
        Greataxe     74     8       0

        Armor:      Cost  Damage  Armor
        Leather      13     0       1
        Chainmail    31     0       2
        Splintmail   53     0       3
        Bandedmail   75     0       4
        Platemail   102     0       5

        Rings:      Cost  Damage  Armor
        Damage +1    25     1       0
        Damage +2    50     2       0
        Damage +3   100     3       0
        Defense +1   20     0       1
        Defense +2   40     0       2
        Defense +3   80     0       3
    '''

    item_shop_parts = item_shop_raw.strip().split('\n\n')
    item_shop = {}
    for p in item_shop_parts:
        item_category = None
        for i, p1 in enumerate(p.split('\n')):
            if i == 0:
                item_category = re.match('(\w+):', p1.strip()).groups()[0]
                item_shop[item_category] = {}
            else:
                props = [x.strip() for x in re.match('(\w+ ?\+?\d?)\s+(\d+)\s+(\d+)\s+(\d+)', p1.strip()).groups()]
                props = [props[0]] + [int(x) for x in props[1:]]
                item_shop[item_category][props[0]] = props[1:]

    hit_points = int(re.match('Hit Points: (\d+)', commands[0]).groups()[0])
    damage = int(re.match('Damage: (\d+)', commands[1]).groups()[0])
    armor = int(re.match('Armor: (\d+)', commands[2]).groups()[0])


    def update_player(player, weapon, armor, rings):
        cost = 0
        if weapon:
            stats = item_shop['Weapons'][weapon]
            player[1] += stats[1]
            cost += stats[0]
        if armor:
            stats = item_shop['Armor'][armor]
            player[2] += stats[2]
            cost += stats[0]
        if rings:
            for r in rings:
                stats = item_shop['Rings'][r]
                player[1] += stats[1]
                player[2] += stats[2]
                cost += stats[0]
        return cost

    def simulate(player, boss):
        turn = 0
        players = [player, boss]
        winner = None
        while True:
            p1, p2 = players[turn % 2], players[(turn + 1) % 2]
            damage = p1[1] - p2[2]
            p2[0] -= max(damage, 1)
            #print 'The {} deals {} damage, the {} goes down to {}'.format(p1[3], damage, p2[3], p2[0])
            if p1[0] > 0 and p2[0] > 0:
                turn += 1
            else:
                winner = p1 if p2[0] == 0 else p2
                break

    weapons = item_shop['Weapons']
    armors = item_shop['Armor']
    rings = item_shop['Rings']


    max_cost = 0
    for iw in range(len(weapons.keys())):
        for ia in range(len(armors.keys()) + 1):
            for pr in range(3):
                for r in itertools.permutations(rings.keys(), pr):
                    w = weapons.keys()[iw]
                    a = armors.keys()[ia] if ia < len(armors) else None

                    player = [100, 0, 0, 'player']
                    boss = [hit_points, damage, armor, 'boss']
                    cost = update_player(player, w, a, r)
                    if cost > max_cost:
                        simulate(player, boss)
                        if boss[0] > 0 and player[0] <= 0:
                            print w, a, r, player, boss, cost
                            print 'updated max cost: {}'.format(cost)
                            max_cost = cost
                    #raw_input()
    print max_cost





if __name__ == '__main__':
    main()
