import turtle
import math
import time

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Heart Equation Animation")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)
pen.color("#FF1493")

text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.color("#FF69B4")

axes = turtle.Turtle()
axes.hideturtle()
axes.speed(0)
axes.pensize(1)
axes.color("#00BFFF")

def draw_axes():
    """Draw coordinate axes"""
    axes.clear()
    axes.penup()
    
    axes.goto(-350, 0)
    axes.pendown()
    axes.goto(350, 0)
    axes.penup()
    
    axes.goto(350, 0)
    axes.setheading(150)
    axes.pendown()
    axes.forward(10)
    axes.penup()
    axes.goto(350, 0)
    axes.setheading(-150)
    axes.pendown()
    axes.forward(10)
    axes.penup()
    
    axes.goto(0, -350)
    axes.pendown()
    axes.goto(0, 350)
    axes.penup()
    
    axes.goto(0, 350)
    axes.setheading(-60)
    axes.pendown()
    axes.forward(10)
    axes.penup()
    axes.goto(0, 350)
    axes.setheading(-120)
    axes.pendown()
    axes.forward(10)
    axes.penup()
    
    for i in range(-3, 4):
        if i != 0:
            axes.goto(i * 80, -5)
            axes.pendown()
            axes.goto(i * 80, 5)
            axes.penup()
            
            axes.goto(-5, i * 80)
            axes.pendown()
            axes.goto(5, i * 80)
            axes.penup()

def heart_equation(x, k):
    """
    Heart equation: y = |x|^(2/3) + 0.9*sin(kx)*sqrt(3-x^2)
    Returns y value for the heart curve
    """
    if abs(x) >= math.sqrt(3):
        return None
    
    try:
        part1 = abs(x) ** (2/3)
        part2 = 0.9 * math.sin(k * x) * math.sqrt(3 - x**2)
        
        y = part1 + part2
        
        return y
    except:
        return None

def draw_heart(k, num_points=800):
    """Draw the heart shape for given k value"""
    pen.clear()
    
    scale = 80
    points = []
    
    x_min = -math.sqrt(3)
    x_max = math.sqrt(3)
    
    for i in range(num_points):
        x = x_min + (x_max - x_min) * i / (num_points - 1)
        y = heart_equation(x, k)
        
        if y is not None:
            points.append((x * scale, y * scale))
    
    if points:
        pen.penup()
        pen.goto(points[0])
        pen.pendown()
        for point in points:
            pen.goto(point)

def update_text(k):
    """Update equation text"""
    text_turtle.clear()
    text_turtle.goto(0, 300)
    text_turtle.write("Heart Equation", align="center", font=("Arial", 20, "bold"))
    
    text_turtle.goto(0, -300)
    equation = "y = |x|^(2/3) + 0.9·sin(kx)√(3-x²)"
    text_turtle.write(equation, align="center", font=("Arial", 12, "normal"))
    
    text_turtle.goto(0, -330)
    text_turtle.write(f"k = {k:.2f}", align="center", font=("Arial", 14, "normal"))

def animate():
    """Main animation function"""
    draw_axes()
    
    # Stage 1
    k_values = [0] * 15
    
    # Stage 2
    for k in [i * 0.1 for i in range(1, 31)]:
        k_values.append(k)
    
    # Stage 3
    for k in [3 + i * 0.25 for i in range(1, 32)]:
        k_values.append(k)
    
    # Stage 4
    for k in [10.75 + i * 1.0 for i in range(1, 40)]:
        k_values.append(k)
    
    for k in k_values:
        draw_heart(k)
        update_text(k)
        screen.update()
        time.sleep(0.04)
    
    time.sleep(2)

animate()

text_turtle.goto(0, -360)
text_turtle.write("Click to close", align="center", font=("Arial", 12, "normal"))
screen.update()
screen.exitonclick()