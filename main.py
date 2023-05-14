turtle.set_position(0, 0)
turtle.turn_right()
turtle.set_speed(20)

def on_forever():
    turtle.forward(4)
    turtle.turn_right()
    turtle.forward(1)
    turtle.turn_right()
    turtle.forward(4)
    turtle.turn_left()
    turtle.forward(1)
    turtle.turn_left()
basic.forever(on_forever)