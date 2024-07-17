import turtle

# Configuração inicial da tartaruga
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.fillcolor("red")
t.speed(2)

# Desenhar o coração
t.hideturtle()
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

# Escrever a string no centro do coração
t.penup()
t.goto(0, 0)
t.setheading(0)
t.color("white")
t.setposition(0,125)
t.write("Amanda", align="center", font=("Arial", 20, "bold"))

# Manter a janela aberta
turtle.done()