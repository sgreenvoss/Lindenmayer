d = 5
angle = 22.5
turtle_pos = [] 
st = True
import random as r


f_list = ['F[+F]F[-F]F', 'F[+F]F', 'F[-F]F']

def pick():
    return r.choice(f_list)

ruleset = { # rule: action
    'F': pick
}

axiom = ['F']
additional_moves = []

# import turtle as td

# def f(turtle):
#     turtle.penup()
#     turtle.forward(d)
#     turtle.pendown()

# def assign_pos(turtle):
#     global turtle_pos 
#     turtle_pos.append((turtle.pos(), turtle.heading()))

# def set_pos(turtle):
#     turtle.penup()
#     global turtle_pos
#     pos, heading = turtle_pos.pop()
#     turtle.goto(pos)
#     turtle.setheading(heading)
#     turtle.pendown()

# move_rules = {
#     'F': lambda turtle: turtle.forward(d),
#     'B': lambda turtle: turtle.forward(d),
#     '-': lambda turtle: turtle.right(angle),
#     '+': lambda turtle: turtle.left(angle),
#     'f': lambda turtle: f(turtle),
#     '[': lambda turtle: assign_pos(turtle),
#     ']': lambda turtle: set_pos(turtle)
# }