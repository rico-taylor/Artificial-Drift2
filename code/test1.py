dictionary = {"hi": 1, 0.00:2.3, "what":"he"}
item = list(dictionary)[0]
print(item)
item2 = dictionary[list(dictionary)[0]]
print(item2)
print(dictionary)