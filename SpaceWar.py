import os
import random
import time



import turtle
#Required by MAC OS
turtle.fd(0)
#Setting the animation speed
turtle.speed(0)
turtle.bgcolor("black")
#background image
turtle.bgpic("SpaceBG.gif")
#Window title
turtle.title("SpaceOdyssey")
#Hiding the default turtle
turtle.ht()
#This saves memory
turtle.setundobuffer(1)
#Speeds up drawing speed
turtle.tracer(0)


class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        #Animation speed not movment.
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        #Movment speed
        self.speed = 1
        
    def move(self):
        self.fd(self.speed)
        
        #Boundary Detection
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)       
            
    #Colliding mechanics
    def is_collision(self,other):
        if(self.xcor() >= (other.xcor() -20)) and \
        (self.xcor() <= (other.xcor() +20)) and \
        (self.ycor() >= (other.ycor() -20)) and \
        (self.ycor() <= (other.ycor() +20)):
         return True
        else:
            return False

class Player(Sprite):
        def __init__(self, spriteshape, color, startx, starty):
            Sprite.__init__(self, spriteshape, color, startx, starty)
            self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
            self.speed = 3
            self.lives = 3
    
        def turn_left(self):
            self.lt(45) 
        def turn_right(self):
            self.rt(45) 
        def accelerate(self):
            self.speed += 1
        def decelerate(self):
            self.speed -= 1
            

class Enemy(Sprite):
        def __init__(self, spriteshape, color, startx, starty):
            Sprite.__init__(self, spriteshape, color, startx, starty)
            self.speed = 3
            self.setheading(random.randint(0,360))
            
class Ally(Sprite):
        def __init__(self, spriteshape, color, startx, starty):
            Sprite.__init__(self, spriteshape, color, startx, starty)
            self.speed = 5
            self.setheading(random.randint(0,360))
            
        def move(self):
            self.fd(self.speed)
        
            #Ally Boundary Detection overwrite
            if self.xcor() > 290:
                self.setx(290)
                self.lt(60)
            if self.xcor() < -290:
                self.setx(-290)
                self.lt(60)
            if self.ycor() > 290:
                self.sety(290)
                self.lt(60)
            if self.ycor() < -290:
                self.sety(-290)
                self.lt(60)       
            
class Missle(Sprite):
        def __init__(self, spriteshape, color, startx, starty):
            Sprite.__init__(self, spriteshape, color, startx, starty)
            self.shapesize(stretch_wid=0.1, stretch_len=0.4, outline=None)
            self.speed = 18 
            self.status = "ready"
            self.goto(-1000, 100)
            

        def fire(self):
            if self.status == "ready":
                self.goto(player.xcor(), player.ycor())
                self.setheading(player.heading())
                self.status = "firing"
                
        def move(self):

            if self.status == "ready":
                self.goto(-1000, 100)
            

            if self.status == "firing":
                self.fd(self.speed)
                
            #Missle border checking
            if self.xcor() < -290 or self.xcor() > 290 or self.ycor() <- 290 or self.ycor() > 290:
                     self.goto(-1000,1000)
                     self.status = "ready"
                
            

class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3
        

    def draw_border(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300,300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()
        
    def show_status(self):
        self.pen.undo()
        msg = "Score: %s" %(self.score)
        self.pen.penup()
        self.pen.goto(-300,310)
        self.pen.write(msg, font=("Arial", 16, "normal"))
        

#game object
game = Game()


#Draw border
game.draw_border()

#Show the scoreboard
game.show_status()



#create sprites
player = Player("triangle", "white", 0, 0)
missle = Missle("triangle", "yellow", 0, 0)

enemies =[]
for i in range (6):
    enemies.append(Enemy("circle","red", -100,0))
    
allys =[]
for i in range (4):
    allys.append(Ally("square", "blue", 250, 0))

#Keyboard binings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missle.fire,"space")
turtle.listen()


#Main game loop
while True:
    turtle.update()
    time.sleep(0.02)
    player.move()
    missle.move()
    
    for ally in allys:
        ally.move()
        
            #check for collision with the player and the Ally
        if player.is_collision(ally):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            ally.goto(x,y)
            game.score -= 200
            game.show_status()
        
        #check for missle hitting Ally
        if missle.is_collision(ally):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            missle.status = "ready"
            ally.goto(x,y)
            game.score -= 50
            game.show_status()
        
    
    
    for enemy in enemies:
        enemy.move()
        
            #check for collision with the player and the Enemy
        if player.is_collision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x,y)
            game.score -= 50
            game.show_status()
        

        #check for missle hitting enemy
        if missle.is_collision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            missle.status = "ready"
            enemy.goto(x,y)
            game.score += 100
            game.show_status()
      
delay = raw_input("Press enter to finish. >")

