# from turtle import *

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "yellow")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokeman Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
table.sortby = "Type"
table.padding_width = 3
print(table)