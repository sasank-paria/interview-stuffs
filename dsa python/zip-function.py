colors = ["brown", "orange", "green", "pink", "purple"]
fruits = ["loquat", "jujube", "pear", "watermelon", "apple"]

for clrs , frts in zip(colors,fruits):
    print(clrs,frts)

for x in zip(colors,fruits):
    print(x)