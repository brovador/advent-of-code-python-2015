#encoding: utf-8
import sys
import os
import re
import string
from operator import add
import itertools
from copy import deepcopy

min_mana_spent = 10000000

def main():
    global min_mana_spent

    script_name = os.path.basename(__file__)
    input_file = './{0}-input.txt'.format(os.path.splitext(script_name)[0])

    with open(input_file, 'r') as f:
        commands = [l.strip() for l in f if l.strip() != '']

    hit_points = int(re.match('Hit Points: (\d+)', commands[0]).groups()[0])
    damage = int(re.match('Damage: (\d+)', commands[1]).groups()[0])

    HIT_POINTS = 0
    MANA = 1
    DAMAGE = 2
    ARMOR = 3

    player = [50, 500, 0, 0]
    boss = [hit_points, 0, damage, 0]

    #player = [10, 250, 0, 0]
    #boss = [14, 0, 8, 0]

    effects = []
    spells = [
        ('Magic Missile', 53),
        ('Drain', 73),
        ('Shield', 113),
        ('Poison', 173),
        ('Recharge', 229),
    ]

    # returns the resutling player, boss and effects
    def simulate(turn, player, boss, effects, mana_spent):

        def log(message):
            pass
            #print ' ' * turn, turn, message

        global min_mana_spent

        if mana_spent >= min_mana_spent:
            return

        player = deepcopy(player)
        boss = deepcopy(boss)
        effects = deepcopy(effects)

        if turn % 2 == 0:
            log('-- Player turn --')
            player[HIT_POINTS] -= 1
            if player[HIT_POINTS] <= 0:
               log('[LOSE] Player has died')
               return
        else:
            log('-- Boss turn --')
        log('- Player has {} hit points, {} armor, {} mana'.format(player[HIT_POINTS], player[ARMOR], player[MANA]))
        log('- Boss has {} hit points'.format(boss[HIT_POINTS]))

        #Apply effects
        player[ARMOR] = 0
        for e in effects:
            if e[0] == 'Shield':
                log('Shield adds 7 armor')
                player[ARMOR] = 7
            elif e[0] == 'Poison':
                log('Poison deals 3 damage')
                boss[HIT_POINTS] -= 3
            elif e[0] == 'Recharge':
                log('Recharge adds 101 mana')
                player[MANA] += 101
            e[1] -= 1
            log('{} timer goes down to {}'.format(e[0], e[1]))
        #remove finished effects
        effects = [e for e in effects if e[1] > 0]

        if boss[HIT_POINTS] <= 0:
            log('[WIN] Boss is killed player wins, {} mana used'.format(mana_spent))
            if mana_spent < min_mana_spent:
                min_mana_spent = mana_spent
            return

        if turn % 2 == 0:
            #players turn
            available_spells = [s for s in spells if s[1] < player[MANA] and not s[0] in [x[0] for x in effects]]
            if not available_spells:
                log('[LOSE] No spells available')
                return
            else:
                current_mana_spent = mana_spent
                current_player = player
                current_boss = boss
                current_effects = effects

                for s in available_spells:

                    mana_spent = current_mana_spent
                    player = deepcopy(current_player)
                    boss = deepcopy(current_boss)
                    effects = deepcopy(current_effects)

                    if s[0] == 'Magic Missile':
                        boss[HIT_POINTS] -= 4
                    elif s[0] == 'Drain':
                        boss[HIT_POINTS] -= 2
                        player[HIT_POINTS] += 2
                    elif s[0] == 'Shield':
                        effects.append(['Shield', 6])
                    elif s[0] == 'Poison':
                        effects.append(['Poison', 6])
                    elif s[0] == 'Recharge':
                        effects.append(['Recharge', 5])

                    player[MANA] -= s[1]
                    mana_spent += s[1]
                    log('Player casts {}'.format(s[0]))

                    if boss[HIT_POINTS] <= 0:
                        log('[WIN] Boss is killed player wins, {} mana used'.format(mana_spent))
                        if mana_spent < min_mana_spent:
                            min_mana_spent = mana_spent
                        return
                    else:
                        simulate(turn + 1, player, boss, effects, mana_spent)

        else:
            #boss turn
            damage = max((boss[DAMAGE] - player[ARMOR]), 1)
            log('{}, {}'.format(player[ARMOR], boss[DAMAGE]))
            player[ARMOR] = max(player[ARMOR] - boss[DAMAGE], 0)
            player[HIT_POINTS] -= damage

            log('Boss attacks for {} damage'.format(damage))

            if player[HIT_POINTS] <= 0:
                log('[LOSE] Player is killed boss wins')
                return

            simulate(turn + 1, player, boss, effects, mana_spent)


    simulate(0, player, boss, effects, 0)
    print min_mana_spent


if __name__ == '__main__':
    main()
