from random import random

from ship import Ship
def create_2d_array(x,y):
    arr = [[0 for i in range(y)] for j in range(x)]
    return arr

def print_array(array):
    for row in array:
     print(row)

array = create_2d_array(10,10)
print_array(array)

ship1 = Ship(1, "mama")
types_of_ships = {"onePole" : 4, "twoPole" : 3, "threePole" :3, "fourPole" : 1}

def put_ship_on_matrix(ship):
    start_x_point = random(0,9)
    start_y_point = random(0,9)

