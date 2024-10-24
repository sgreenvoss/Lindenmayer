# controllable model
import l
import simple_gui


class View():
    def __init__(self, turtle, screen) -> None:
        self.t = turtle
        self.screen = screen
        self.rotation_angle = 10
        self.translation = 20
       

    
    def make_default_moves(self):
        turtle_pos = []
        move_rules = {
            'F': lambda turtle: turtle.forward(self.d),
            'B': lambda turtle: turtle.forward(self.d),
            'X': lambda turtle: None,
            '-': lambda turtle: turtle.right(self.angle),
            '+': lambda turtle: turtle.left(self.angle),
            'f': lambda turtle: f(turtle),
            '[': lambda turtle: assign_pos(turtle),
            ']': lambda turtle: set_pos(turtle)
        }

        def f(turtle):
            turtle.penup()
            turtle.forward(self.d)
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
# ---------------------------------------------#
# L-SYSTEM MANAGEMENT

    def set_system(self, system):
        self.system = system
        self.d, self.angle = self.system.give_distance_angle()
        self.init_d, self.init_angle = self.system.give_distance_angle()
        self.move_rules = self.make_default_moves()
        for char, rule in self.system.additional_moves:
            self.move_rules[char] = rule
        self.current_str = system.get_string(1)
        self.st = system.st
        self.root = (0,0)
        self.root_head = 90
        self.curr = 0

    def get_string(self, n):
        """
        Returns string at iteration n
        """
        self.curr = n
        return self.system.get_string(n)
    
    def set_string(self, n):
        self.curr = n
        self.current_str = self.system.get_string(n)

    def turt_ex(self, ax, t):
        self.root = self.t.pos()
        for i in ax:
            self.move_rules[i](t)

    def turtle_run(self):
        self.set_listeners()
        print(f"\ncurrent string: {self.current_str}")
        self.t.speed(0)
        self.screen.tracer(0)
        self.t.clear()
        self.t.goto(self.root)
        self.t.setheading(self.root_head)
        self.draw_latest()

    def draw_latest(self):
        self.t.clear()
        self.t.hideturtle()
        self.turt_ex(self.current_str, self.t)
        self.screen.update()

    def move(self, dx, dy):
        self.t.clear()
        self.t.penup()
        x, y = self.root
        # print(f"Moving from ({x}, {y}) by ({dx}, {dy})")
        self.t.goto(x + dx, y + dy)
        self.t.setheading(self.root_head)
        self.root = self.t.pos()
        # print(f"New position: {self.root}")
        self.t.pendown()
        self.draw_latest()

    def rotate(self):
        self.t.clear()
        self.t.penup()
        self.t.goto(self.root)
        head = self.t.heading()
        # print(f"Rotating from {head} by {rotation_angle}")
        ra = head + self.rotation_angle
        self.t.setheading(ra)
        self.root_head = self.t.heading()
        self.t.pendown()
        self.draw_latest()

    def rotater(self):
        self.t.clear()
        self.t.penup()
        self.t.goto(self.root)
        self.t.pendown()
        head = self.t.heading()
        self.t.setheading(head - self.rotation_angle)
        self.root_head = self.t.heading()
        self.draw_latest()

    def get_screen(self):
        return self.screen

    def tell(self, info):
        message, data = info
        match message: 
            case 'ITER':
                self.set_string(data)
                self.turtle_run()
            case 'SYST':
                new_system = l.LSystem(data)
                self.set_system(new_system)
                print('new system set')
            case 'CLEAR':
                self.screen.clear()
            case 'RUN':
                iterations, distance, angle = data
                self.set_string(iterations)
                self.d = distance
                self.angle = angle
                self.turtle_run()
            case 'RESET':
                self.d, self.angle = self.system.give_distance_angle()

    def give_angle_distance(self):
        return self.init_angle, self.init_d
        

#------------------------------------------------

    def tu(self):
        self.move(0, self.translation)

    def td(self):
        self.move(0, -self.translation)

    def tl(self):
        self.move(-self.translation, 0)

    def tr(self):
        self.move(self.translation, 0)

    def stamp(self):
        self.t = l.turtle.Turtle()
        self.root = 0, 0
        self.current_str = self.get_string(self.curr)

    def set_listeners(self):
        self.screen.listen()
        l.turtle.onkey(self.rotate, "Left")
        l.turtle.onkey(self.tu, "w")
        l.turtle.onkey(self.tl, "a")
        l.turtle.onkey(self.td, "s")
        l.turtle.onkey(self.tr, "d")
        l.turtle.onkey(self.rotater, "Right")
        l.turtle.onkey(self.stamp, 'Return')

def main():
    screen = l.turtle.Screen()
    turtle = l.turtle.Turtle()
    view = View(turtle, screen)
    l_system = l.LSystem(f'systems.deterministic.koch')
    view.set_system(l_system)
    view.set_string(5)
    view.set_listeners()
    gui = simple_gui.Gui()
    gui.listeners.append(view)
    gui.get_set_angle_distance()
    view.turtle_run()
    screen.mainloop()

main()