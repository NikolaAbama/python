import time
a = 0
x = 300
y = 200
z = 90
v = 90
y1 = -500
y2 = -1050
y3 = -1300
y4 = -750
y5 = -1550
y6 = -2050
y7 = -1800
y8 = -3200
y9 = -3500
y10 = -4750
x1 = 0
x2 = 150
x3 = 300
x4 = 400
x5 = 320
x6 = 200
x7 = 230
x8 = 330
x9 = 270 
x10 = 290
def setup():
    global a,x,y,z,v,y2,x3,x4,x5
    size(600,400)
    a = loadImage("game_over_PNG57.png")
def star(x, y):
    push()
    translate(x,y)
    fill(15,255,33)
    rect(100,100,30,30)
    fill(0,0,0)
    triangle(130,100,175,115,130,130)
    triangle(100,100,115,50,130,100)
    triangle(100,130,55,115,100,100)
    triangle(115,175,100,130,130,130)
    pop()
def draw():
    global x,y,z,v,y1,a,y2,y3,y4,y5,y6,y7,y8,y9,y10,x1,x2,x3,x4,x5,x6,x7,x8,y9,y10
    background(255)
    fill(250,255,0)
    ellipse(x,y,z,v)
    y1 = y1 + 1
    y2 = y2 + 1
    y3 = y3 + 1
    y4 = y4 + 1
    y5 = y5 + 1
    y6 = y6 + 1
    y7 = y7 + 1
    y8 = y8 + 1
    y9 = y9 + 1
    y10 =y10 +1
    star(x1, y1)
    star(x2, y2)
    star(x3, y3)
    star(x4, y4)
    star(x5, y5)
    star(x6, y6)
    star(x7, y7)
    star(x8, y8)
    star(x9, y9)
    star(x10, y10)
    if y2>=400:
       y2=-150
    if x>=55 and x<=215 and y>=y2+50 and y<=220+y2:
       image(a,0,0,600,400)
       #time.sleep(5)
       exit()
    if x+z>=55+x1 and x-z<=175+x1 and y+v>=50+y1 and y-v<= 175+y1:
        exit()
    if x+z>=55+x2 and x-z<=175+x2 and y+v>=50+y3 and y-v<=175+y2:
        exit()
    if x+z>=55+x3 and x-z<=175+x3 and y+v>=50+y3 and y-v<=175+y3:
        exit()
    if x+z>=55+x4 and x-z<=175+x4 and y+v>=50+y4 and y-v<=175+y4:
        exit()
    if x+z>=55+x5 and x-z<=175+x5 and y+v>=50+y5 and y-v<=175+y5:
        exit()
    if x+z>=55+x6 and x-z<=175+x6 and y+v>=50+y6 and y-v<=175+y6:
        exit()
    if x+z>=55+x7 and x-z<=175+x7 and y+v>=50+y7 and y-v<=175+y7:
        exit()
    if x+z>=55+x8 and x-z<=175+x8 and y+v>=50+y8 and y-v<=175+y8:
        exit()
    if x+z>=55+x9 and x-z<=175+x9 and y+v>=50+y9 and y-v<=175+y9:
        exit()
    if x+z>=55+x10 and x-z<=175+x10 and y+v>=50+y10 and y-v<=175+y10:
        exit()


    if x>=600-z/2: 
        x = 600-z/2
    if y>=400-v/2:
        y = 400-v/2
    if x<0+z/2:
        x = 0+z/2
    if y<0+v/2:
        y = 0+v/2

def keyPressed():
    global x,y,z,v
    if key == CODED:
         if keyCode == UP:
             y = y - 5
         if keyCode == DOWN:
             y = y + 5
         if keyCode == LEFT:
             x = x - 5
         if keyCode == RIGHT:
             x = x + 5
    if key == "g" or key == "G" or key == "п" or key == "П":
       z = z + 30
       v = v + 30
       if z>=90 and v>=90:
           z = 90 
           v = 90        
    if key == "f" or key == "F" or key == "а" or key == "А":
       v = v - 30
       z = z - 30    
       if z<=0 and v<=0:
           z = 30 
           v = 30
