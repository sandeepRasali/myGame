import turtle as trt
import random
import math
# import numpy as np


wn = trt.Screen()
wn.bgcolor('black')
wn.title("Air Strike")
wn.bgpic('background.gif')


# trt.register_shape('')
trt.register_shape('player.gif')
trt.register_shape('bullet.gif')
trt.register_shape('enemy.gif')

test = trt.Turtle()
test.pu()
test.color('red')
test.setposition(90 ,320)

player = trt.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(-500, 150)
player.setheading(0)



playerSpeed = 50

bullet = trt.Turtle()
bullet.shape("bullet.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

ebullet = trt.Turtle()
ebullet.shape('bullet.gif')
ebullet.pu()
ebullet.speed(0)
ebullet.setheading(180)
ebullet.hideturtle()



number_of_enemies = 4


# list for storing the enemies
enemies = []

# using append method of list to add enemies in the list
for i in range(number_of_enemies):
    # create the enemy
    enemies.append(trt.Turtle())

for enemy in enemies:
    #enemy.color("Red")
    enemy.shape("enemy.gif")
    enemy.color('red')
    enemy.rt(180)
    enemy.penup()
    enemy.speed(0)
    x = random.randint(50, 400)
    y =  random.randint(50, 200 )
    enemy.setposition(x, y)

enemyspeed = 7


def move_left():
    x = player.xcor()
    x -= playerSpeed
    if x < -515:
        x = -515
    player.setx(x)

    
def move_right():
    x = player.xcor()
    x += playerSpeed
    if x > 515:
        x = 515
    player.setx(x)

    
def move_up():
    x = player.ycor()
    x += playerSpeed
    if x > 310:
        x = 310
    player.sety(x)

    
def move_down():
    x = player.ycor()
    x -= playerSpeed
    if x < -280:
        x = -280
    player.sety(x)
    
    
    
bulletSpeed = 10
bulletstate = 'ready'
ebulletstate = 'eready'
    
def fire_bullet():
    
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # Move the bullet to the just above the player
        # winsound.PlaySound("laser.wav", winsound.SND_ASYNC) #sound for windows
        #os.system("aplay laser.wav&") #sound for linux
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()


def enemy_bullet():
     global ebulletstate
    
     if ebulletstate == "eready":
        ebulletstate = "efire"
      
        x = enemy.xcor()
        y = enemy.ycor() + 10
        ebullet.setposition(x,y)
        ebullet.showturtle()

    




trt.listen()
trt.onkey(move_left, "Left")
trt.onkey(move_right, "Right")
trt.onkey(move_up, "Up")
trt.onkey(move_down, "Down")
trt.onkey(fire_bullet, "space")




# Main loop for the game
Game_Over = False
missed_enemies = 0
while True:

    for enemy in enemies:
        x = enemy.xcor()            # moving the enemy
        x += enemyspeed
        enemy.setx(x)
        
    
        if enemy.xcor() > 530:
            for x in enemies:
                y = x.ycor()
                y -= random.randint(0, 20)
                x.sety(y)
                
            enemyspeed *= -1
        
        if enemy.xcor() < 110:
            for x in enemies:
                y = x.ycor()
                y += random.randint(0, 40)
                x.sety(y)
                
            enemyspeed *= -1
            
            
            
            
            
            
            
            
            
            
            
            

    if bulletstate == "fire":           # moving the bullet
        y = bullet.xcor()
        y += bulletSpeed
        # bullet.speed(8)
        bullet.setx(y)

  
    if bullet.xcor() > 540:                 # checking the position of bullet
        bullet.hideturtle()
        bulletstate = "ready"
        
    for enemy in enemies:
        enemy_bullet()                      # calling the function to initiate the enemy bullet
            
        if ebulletstate == "efire":
            y = ebullet.xcor()
            y -= bulletSpeed
            # ebullet.speed(8)
            ebullet.setx(y)


        if ebullet.xcor() < -500:
            ebullet.hideturtle()                    # checking the position of bulletf
            ebulletstate = "eready"
            


trt.done()