import turtle as tt
import time

tt.bgcolor('black')
tt.pensize(2)
tt.speed(8)

for i in range(6):
    for color in ('cyan', 'green', 'blue',
                  'red', 'green', 'white',
                  'yellow', 'green', 'orange'):
        tt.color(color)
        tt.circle(100)
        tt.left(10)
    tt.hideturtle()
