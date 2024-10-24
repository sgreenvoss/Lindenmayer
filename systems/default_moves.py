def make_default_moves(d, angle):
    turtle_pos = []
    move_rules = {
        'F': lambda turtle: turtle.forward(d),
        'X': lambda turtle: None,
        '-': lambda turtle: turtle.right(angle),
        '+': lambda turtle: turtle.left(angle),
        'f': lambda turtle: f(turtle),
        '[': lambda turtle: assign_pos(turtle),
        ']': lambda turtle: set_pos(turtle)
    }

    def f(turtle):
        turtle.penup()
        turtle.forward(d)
        turtle.pendown()

    def assign_pos(turtle):
        turtle_pos.append((turtle.pos(), turtle.heading()))

    def set_pos(turtle):
        turtle.penup()
        pos, heading = turtle_pos.pop()
        turtle.goto(pos)
        turtle.setheading(heading)
        turtle.pendown()

    return move_rules