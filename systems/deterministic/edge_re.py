d = 3
angle = 20
turtle_pos = [] # this is probably a problem


# TODO: fix rotation on this guy

ruleset = { # rule: action
    'F': "FF",
    'X': "F[+X]F[-X]+X"
}

axioms = ['X']

import turtle as td

def f(turtle):
    turtle.penup()
    turtle.forward(d)
    turtle.pendown()

def assign_pos(turtle):
    global turtle_pos 
    turtle_pos.append((turtle.pos(), turtle.heading()))

def set_pos(turtle):
    turtle.penup()
    global turtle_pos
    pos, heading = turtle_pos.pop()
    turtle.goto(pos)
    turtle.setheading(heading)
    turtle.pendown()

move_rules = {
    'F': lambda turtle: turtle.forward(d),
    'X': lambda turtle: None,
    '-': lambda turtle: turtle.right(angle),
    '+': lambda turtle: turtle.left(angle),
    'f': lambda turtle: f(turtle),
    '[': lambda turtle: assign_pos(turtle),
    ']': lambda turtle: set_pos(turtle)
}