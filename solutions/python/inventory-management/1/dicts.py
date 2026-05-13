"""Functions to keep track and alter inventory."""


def create_inventory(items):
    inventory = {}
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

def add_items(inventory, items):
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] = max(0, inventory[item] - 1)
    return inventory

def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    for item in inventory:
        return [(item, qty) for item, qty in inventory.items() if qty > 0]