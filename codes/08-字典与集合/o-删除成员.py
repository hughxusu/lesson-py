colors = {'red', 'blue', 'yellow', 'purple'}

colors.remove('red')
print(colors)
colors.remove('red')

colors.discard('yellow')
print(colors)
colors.discard('yellow')

color = colors.pop()
print(colors)
print(color)

colors.clear()