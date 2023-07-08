def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for (item, count) in inventory.items():# unpack variables into inventory. (key,value) items() key-value pairs of the dictionary as tuples.
        item_total += count # prints what number item in the list then item_total becomes that number 
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    for item in addedItems:#count goes up ever time it iternated over an item in the inventory 
        inventory.setdefault(item, 0) #use .setdefault(key,value) built in to set item = 0
        inventory[item] += 1 #increments the count of item by 1 when item 
    print('Inventory updated!')


def main():
    stuff = {'rope': 1, 'gold coin': 42, 'dagger': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    displayInventory(stuff)
    addToInventory(stuff, dragonLoot)
    print('The dragon has been vanquished! Looting...')
    displayInventory(stuff)


main()


stuff = {'rope': 1, 'gold coin': 42, 'dagger': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(stuff)

stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
print('The dragon has been vanquished! Looting...')





main() #call to main to start executing the code
