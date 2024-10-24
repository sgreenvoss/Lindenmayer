"""
basic L-system read and write
"""
import turtle
# from systems.deterministic.bigger import *
from systems.deterministic.messy import *
# from systems.deterministic.sprig import *
# from systems.stochastic.branch import *
# from systems.deterministic.koch import *
# from systems.deterministic.another_tree import *
import importlib


# def make_default_moves(d, angle):
#     turtle_pos = []
#     move_rules = {
#         'F': lambda turtle: turtle.forward(d),
#         'B': lambda turtle: turtle.forward(d),
#         'X': lambda turtle: None,
#         '-': lambda turtle: turtle.right(angle),
#         '+': lambda turtle: turtle.left(angle),
#         'f': lambda turtle: f(turtle),
#         '[': lambda turtle: assign_pos(turtle),
#         ']': lambda turtle: set_pos(turtle)
#     }

#     def f(turtle):
#         turtle.penup()
#         turtle.forward(d)
#         turtle.pendown()

#     def assign_pos(turtle):
#         turtle_pos.append((turtle.pos(), turtle.heading()))

#     def set_pos(turtle):
#         turtle.penup()
#         pos, heading = turtle_pos.pop()
#         turtle.goto(pos)
#         turtle.setheading(heading)
#         turtle.pendown()

#     return move_rules

class LSystem():
    def __init__(self, file) -> None:
        self.file = file
        self.set_from_file()
        # self.move_rules = make_default_moves(self.distance, self.angle)
        # for char, rule in self.additional_moves:
        #     self.move_rules[char] = rule

    def set_from_file(self):
        l = importlib.import_module(self.file)
        self.axiom = l.axiom
        self.angle = l.angle
        self.distance = l.d
        self.ruleset = l.ruleset
        self.st = l.st
        self.additional_moves = l.additional_moves
        

    def replace(self, word):
        nw = ''
        for i in range(len(word)):
            if word[i] in self.ruleset:
                if self.st:
                    nw += self.ruleset[word[i]]()
                else:
                    nw += self.ruleset[word[i]]
            else:
                nw += word[i]
        # print('word:', nw)
        return nw
    
    def get_string(self, n):
        st = self.axiom
        for _ in range(0, n + 1):
            st = self.replace(st)
        return st

    def give_distance_angle(self):
        return self.distance, self.angle
    
    # def get_move_rules(self):
    #     return self.move_rules
    