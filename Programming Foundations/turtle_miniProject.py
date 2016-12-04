import turtle

def draw_squares(some_turtle):
    for x in range(0,2):
        some_turtle.forward(100)
        some_turtle.right(45)
        some_turtle.forward(100)
        some_turtle.right(135)



def draw_circle(circle_turtle):
   circle_turtle.circle(100)

def draw_triangle(triangle_turtle):

    for y in range(0,3):
        triangle_turtle.right(120)
        triangle_turtle.forward(40)


def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle();
    brad.shape("turtle")
    brad.speed(10)
    brad.settiltangle(100)
    brad.color("blue", "green")
    for x in range(0,36): 
        draw_squares(brad)
        brad.right(10)
    brad.seth(270)
    brad.forward(300)
                 
draw_shapes()
