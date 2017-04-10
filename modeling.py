import pygal
from die import Die
# Make two dies
die1 = Die()
die2 = Die()
# Make some results
result = [die1.roll() * die2.roll() for i in range(100000)]
# Count number of each number
frequencies = [result.count(val) for val in range(1, die1.num_sides * die2.num_sides + 1)]
hist = pygal.Bar()
# Titles
hist.title = "Result of rolling one D6 10000 times"
hist.x_labels = list(i for i in range(1, 37))
hist.x_title = "Result"
hist._y_title = "Frequency of result"
hist.add("D", frequencies)
# Make a file
hist.render_to_file("die_visual_two.svg")
