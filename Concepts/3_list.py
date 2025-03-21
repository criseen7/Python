#LISTS
shoppingList = ['apples', 'bananas', 'oranges', 'cheese']
print(shoppingList)
print(shoppingList[0])
print(shoppingList[0:4:2])

#add items in our list
shoppingList.append('blueberries')
print(shoppingList)

#update items in our list
shoppingList[1] = 'cherries'
print(shoppingList)

#delete items
del shoppingList[2]
print(shoppingList)

#length of list
print(len(shoppingList))

shoppingList2 = ['bread','jam','butter peanut']
print(shoppingList + shoppingList2)
print(shoppingList2 * 2)

#max and min
listNum = [1,4,7,68,13]
print(max(listNum))
print(min(listNum))

