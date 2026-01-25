import turtle
import math
import time

# Setup screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Heart Equation Animation")
screen.tracer(0)

# Create turtle for drawing
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)
pen.color("#FF1493")

# Create turtle for text
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.color("#FF69B4")

# Create turtle for axes
axes = turtle.Turtle()
axes.hideturtle()
axes.speed(0)
axes.pensize(1)
axes.color("#00BFFF")

def draw_axes():
    """Draw coordinate axes"""
    axes.clear()
    axes.penup()
    
    # X-axis
    axes.goto(-350, 0)
    axes.pendown()
    axes.goto(350, 0)
    axes.penup()
    
    # Arrows for x-axis
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
    
    # Y-axis
    axes.goto(0, -350)
    axes.pendown()
    axes.goto(0, 350)
    axes.penup()
    
    # Arrows for y-axis
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
    
    # Tick marks
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

def heart_polar(t, k):
    """
    Heart shape in polar coordinates with modulation
    r = 1 - sin(t) + modulation
    """
    # Basic heart curve
    r = 2 - 2 * math.sin(t) + math.sin(t) * math.sqrt(abs(math.cos(t))) / (math.sin(t) + 1.4)
    
    # Add oscillation based on k
    if k > 0:
        modulation = 0.15 * math.sin(k * t)
        r = r * (1 + modulation)
    
    x = r * math.cos(t)
    y = r * math.sin(t)
    
    return x, y

def draw_heart(k, num_points=1000):
    """Draw the heart shape for given k value"""
    pen.clear()
    pen.penup()
    
    points = []
    
    # Generate points around the heart
    for i in range(num_points + 1):
        t = 2 * math.pi * i / num_points
        x, y = heart_polar(t, k)
        points.append((x * 60, y * 60 - 30))  # Scale and shift
    
    # Draw the heart
    if points:
        pen.goto(points[0])
        pen.pendown()
        for point in points:
            pen.goto(point)

def update_text(k):
    """Update equation text"""
    text_turtle.clear()
    text_turtle.goto(0, 300)
    text_turtle.write("Heart Equation", align="center", font=("Arial", 20, "bold"))
    
    # Equation
    text_turtle.goto(0, -300)
    equation = f"y = |x|^(2/3) + 0.9·sin(kx)√(3-x²)"
    text_turtle.write(equation, align="center", font=("Arial", 12, "normal"))
    
    text_turtle.goto(0, -330)
    text_turtle.write(f"k = {k:.2f}", align="center", font=("Arial", 14, "normal"))

def animate():
    """Main animation function"""
    draw_axes()
    
    # Stage 1: k = 0 (smooth heart)
    k_values = [0] * 20  # Hold at k=0
    
    # Stage 2: k increases to 3 (wavy)
    for k in [i * 0.05 for i in range(1, 61)]:
        k_values.append(k)
    
    # Stage 3: k increases to 10 (more oscillations)
    for k in [3 + i * 0.15 for i in range(1, 48)]:
        k_values.append(k)
    
    # Stage 4: k increases to 50 (very dense oscillations)
    for k in [10 + i * 0.8 for i in range(1, 51)]:
        k_values.append(k)
    
    # Animate through k values
    for k in k_values:
        draw_heart(k)
        update_text(k)
        screen.update()
        time.sleep(0.03)
    
    # Hold final frame
    time.sleep(2)

# Run animation
animate()

# Keep window open
text_turtle.goto(0, -360)
text_turtle.write("Click to close", align="center", font=("Arial", 12, "normal"))
screen.update()
screen.exitonclick()