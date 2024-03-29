import turtle
import winsound

wn = turtle.Screen()
wn.title("Revant's Pong game")
wn.bgcolor("black")
wn.setup(width=800, height= 600)
wn.tracer(0) 
# tracer allows  us to manually update a screen 
#---> allowing game to run faster 

# Paddle No-1

paddle_1 = turtle.Turtle() # -> created the object paddle 1 
paddle_1.speed(0)  # -> Gives us the maximum speed (Speed of animation not the speed of paddle)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5,stretch_len=1)
paddle_1.penup() #-> in logo young class tortoise makes line we dont want that thats why penup
paddle_1.goto(-350,0) # -> Setting up the coordinates (0,0) is the middle 

# Paddle No-2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.color("white")
paddle_2.shape("square")
paddle_2.penup()
paddle_2.goto(350,0)
paddle_2.shapesize(stretch_wid=5,stretch_len=1)

#score
player_1_score = 0
player_2_score = 0

#Pen

pen =turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(0,260)
pen.color("white")
pen.hideturtle()
pen.write("Welcome to Revant's Pong",align="center",font=("Arial",20,"bold"))

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("square")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2
# Moving Paddle 1 with function
def paddle_1_up():
    y = paddle_1.ycor() # -> giving y the y coordinate of our turtle/ paddle 1 
    y+=20
    paddle_1.sety(y) # -> setting y coordinate of paddle 1 with the new y coordinate value

def paddle_1_down():
    y = paddle_1.ycor() # -> giving y the y coordinate of our turtle/ paddle 1 
    y-=20
    paddle_1.sety(y) # -> setting y coordinate of paddle 1 with the new y coordinate value    

# Moving paddle 2 with function
def paddle_2_up():
    y = paddle_2.ycor() 
    y+=20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

# Keyboard bind
wn.listen() #-> telling the turtle to listen for inputs
wn.onkeypress(paddle_1_up,"w") # -> telling turtle to execute function paddle1up when w key is pressed  // goes up
wn.onkeypress(paddle_1_down,"s") # -> goes down 
wn.onkeypress(paddle_2_up,"Up")
wn.onkeypress(paddle_2_down,"Down")

# Main game loop starts 

while True:
    wn.update()  #-> whenever the loop runs it updates the screen

    # MOving the ball
    ball.setx(ball.xcor() + ball.dx) 
    ball.sety(ball.ycor()+ ball.dy)
    
    #Setting border
    if ball.ycor() > 290:
        winsound.PlaySound("D:/prac/pong/bounce.wav", winsound.SND_ASYNC)

        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        winsound.PlaySound("D:/prac/pong/bounce.wav", winsound.SND_ASYNC)

        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        player_1_score += 1
        pen.clear()
        pen.write("Player 1 : {}     Player 2 : {}".format(player_1_score,player_2_score),align="center",font=("Arial",20,"bold"))
        ball.goto(0,0)
        ball.dx *= -1
    
    if ball.xcor() < -390:
        pen.clear()
        player_2_score +=1
        pen.write("Player 1 : {}     Player 2 : {}".format(player_1_score,player_2_score),align="center",font=("Arial",20,"bold"))
        ball.goto(0,0)
        ball.dx *= -1

    # Collision 
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40) :
        ball.setx(340)
        winsound.PlaySound("D:/prac/pong/bounce.wav", winsound.SND_ASYNC)
        ball.dx *= -1
    
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() -40) :
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("D:/prac/pong/bounce.wav", winsound.SND_ASYNC)

