#!/bin/bash
import argparse
import os
import sys

import numpy

from itertools import count, izip, repeat, product, chain

class Ship(object):
    def __init__(self, name, hull, count, speed):
        self.name = name
        self.hull = hull
        self.count = count
        self.speed = speed
        self.owner = None # not set yet

    def __repr__(self):
        return self.name + " " + self.owner

    def __str__(self):
        return self.name

    # order ships by initiaitive
    def __cmp__(self, other):
        if self.speed < other.speed:
            return -1
        if self.speed == other.speed:
            if self.owner == "attacker":
                return -1
            return cmp(self.name, other.name)
        return 1

def ship_states(ships):
    ship_states = []
    for ship in ships:
        ship_state = product(range(ship.hull), range(ship.count+1))
        labeled_states = izip(repeat(ship), ship_state)
        ship_states.append(labeled_states)
    ships = product(*ship_states)
    return ships

def own_ships(ships, owner):
    for ship in ships:
        ship.owner = owner

def construct_states(defender_ships, attacker_ships):
    states = []
    ships = set(defender_ships).union(set(attacker_ships))
    dships = ship_states(defender_ships)
    aships = ship_states(attacker_ships)
    ships_state = product(aships, dships)
    combat_state = product(ships_state, ships)
    return list(reversed(sorted(defender_ships + attacker_ships))), {state: 0 for state in combat_state}

def find_initial_state(probs, order):
    for state in probs:
        ((attackers), (defenders)), current = state
        if current != order[0]:
            continue
        all_undamaged = True
        for ship in chain(attackers, defenders):
            s, (damage, count) = ship
            if not (s.count == count and damage == 0):
                all_undamaged = False
        if all_undamaged:
            return state

def all_destroyed(ships):
    for ship, (count, damage) in defender_ships:
        if count != 0:
            return False
    return True

def assign_damage(target_ships, dice):
    # can destroy a ship?
    remaining_dice = list(dice)
    for die in dice:
        if die == 6:
    # Hit the biggest one
    

def successor_states(state, order);
    (defender_ships, attacker_ships), current_ship = state
    ships = defender_ships + attacker_ships
    # Check for Victory
    if all_destroyed(defender_ships):
        return []
    if all_destroyed(attacker_ships):
        return []
    states = []
    for ship, _ in defender_ships+attacker_ships:
        
    next_ship = order[(order.index(current_ship) + 1) % len(order)]
        

def compute_probs(order, probs, ):
    matrix = sparse
    state_indices = {state : idx for (idx, state) in enumerate(states)}
    for state in states:
        state_idx = state_indices[state]
        for successor in successor_states(state, order):
            successor_idx = state_indices[successor]
            matrix[state_idx, successor_idx] = transition_prob(state, successor)
        

def main(args):
    parser = argparse.ArgumentParser()
    options = parser.parse_args(args)
    defenders = [Ship("Interceptor", 3, 8, 3), Ship("Cruiser", 2, 3, 2)]
    own_ships(defenders, "defender")
    attackers = [Ship("Dreadnought", 3, 2, 1)]
    own_ships(attackers, "attacker")
    order, probs = construct_states(defenders, attackers)
    initial_state = find_initial_state(probs, order)
    probs[initial_state] = 1.0
    compute_probs(order, probs, state)

if __name__ == "__main__":
    main(sys.argv[1:])
