"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    if power_pellet_active and touching_ghost:
        return True
    else:
        return False

def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot

def lose(power_pellet_active, touching_ghost):
    return not power_pellet_active and touching_ghost

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    return not touching_ghost or power_pellet_active and has_eaten_all_dots