def update_inventory(inventory, shipment):
    for ship in shipment:
        found = False
        for element in inventory:
            if ship[1] == element[1]:
                element[0] += ship[0]
                found = True
                break
        if not found:
            inventory.append(ship)
            
    return inventory

print(update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]]))
print(update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]]))
print(update_inventory([], [[10, "apples"], [30, "bananas"], [20, "oranges"]]))
print(update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]))

