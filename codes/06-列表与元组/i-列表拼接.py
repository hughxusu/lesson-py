colors = ['red', 'green', 'blue', 'yellow', 'white', 'black']
colors.append(['purple', 'pink'])
print(colors)

colors = ['red', 'green', 'blue', 'yellow', 'white', 'black']
colors.extend(['purple', 'pink'])
print(colors)

colors = ['red', 'green', 'blue', 'yellow', 'white', 'black']
short_colors = ['purple', 'pink']

colors_all = colors + short_colors
print(colors)
print(colors_all)
print(short_colors)

colors += short_colors
print(colors)

colors *= 2
print(colors)