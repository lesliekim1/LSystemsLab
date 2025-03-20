import random
import turtle

# Set screen boundaries
BOUNDX = 300
BOUNDY = 300

# Generate and draw the L-Systems with three turtles
def main():
    my_rules = {
        'A': ['A', 'B', 'C', 'A'],
        'B': ['B', 'C', 'A', 'B', 'B'],
        'C': ['A', 'C', 'C', 'B', 'A']
    }

    my_rules2 = {
        'A': ['C', 'A', 'B', 'C', 'C'],
        'B': ['A', 'C', 'B', 'A', 'A'],
        'C': ['B', 'A', 'C', 'C', 'B']
    }

    my_rule_table = [my_rules, my_rules2]
    my_axiom = ['A']

    # Generate L-Systems sequence with multiple iterations
    for i in range(7):
        my_axiom = lindemayer_translation(random.choice(my_rule_table), my_axiom)

    print("Final result:", "".join(my_axiom))
    draw_lsystem(my_axiom)

# Applies L-System rules to transform the axiom iteratively.
def lindemayer_translation(rules, axiom):
    translated = []

    for symbol in axiom:
        if symbol in rules:
            translated.extend(rules[symbol])
        else:
            # unchanged
            translated.append(symbol)

    return translated

# Check if turtle is out of boundary
def is_out_of_bounds(t):
    x, y = t.xcor(), t.ycor()
    return abs(x) > BOUNDX or abs(y) > BOUNDY

# Creates a new turtle with a specified color, starting position, and direction
def create_turtle(color, start_pos, angle):
    t = turtle.Turtle()
    t.speed(-1)
    t.color(color)
    t.penup()
    t.goto(start_pos)
    t.setheading(angle)
    t.pendown()
    return t

# Draw with 3 turtles
def draw_lsystem(axiom, step=10, angle=45):
    turtle.bgcolor("black")
    turtle.colormode(255)

    # Initialize 3 turtles with different colors, positions, and angles
    turtles = [
        create_turtle("red", (-100, 0), random.randint(0, 360)),
        create_turtle("green", (0, -100), random.randint(0, 360)),
        create_turtle("blue", (100, 100), random.randint(0, 360))
    ]

    color_shift = [0, 50, 100]
    directions = [1, 1, 1]

    for symbol in axiom:
        for i, t in enumerate(turtles):
            # Cycle colors
            r = (color_shift[i] % 255)
            g = (color_shift[i] * 2 % 255)
            b = (color_shift[i] * 3 % 255)
            t.pencolor(r, g, b)

            # movements
            if symbol in ['A', 'B']:
                t.forward(step * directions[i])
            elif symbol == 'C':
                t.left(angle * directions[i])
            else:
                t.right(angle * directions[i])

            # Reverse direction if out of boundary
            if is_out_of_bounds(t):
                directions[i] *= -1
                t.right(180)
            color_shift[i] += 10
    turtle.done()

main()
