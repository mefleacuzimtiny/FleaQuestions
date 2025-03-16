# Quadratic question generator

import random

def numGen():
    return [random.randint(1, 20) for i in range(4)]

def sign():
    return random.choice(['+', '-'])

def left_signs():
    return random.choice(['', '-'])

def combinations():                                    # (ax b cx d) (a bx c dx) (ax b c dx) (a bx cx d)
    a, b, c, d = numGen()
    return random.choice([
        f"({left_signs()}{a}x {sign()} {b})({left_signs()}{c}x {sign()} {d})",
        f"({left_signs()}{a}x {sign()} {b})({left_signs()}{c} {sign()} {d}x)",
        f"({left_signs()}{a} {sign()} {b}x)({left_signs()}{c}x {sign()} {d})",
        f"({left_signs()}{a} {sign()} {b}x)({left_signs()}{c} {sign()} {d}x)"
        ])

for i in range(10):
    print(str(i+1)+ ". " + combinations())
    print()

input()
