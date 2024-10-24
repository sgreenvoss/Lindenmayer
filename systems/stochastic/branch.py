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
