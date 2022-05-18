x = 300
y = 200
z = 90
v = 90
y2 = 0
def setup():
    size(600,400)
    
def star():
    push()
    fill(15,255,33)
    rect(100,100,30,30)
    fill(0,0,0)
    triangle(130,100,175,115,130,130)
    triangle(100,100,115,50,130,100)
    triangle(100,130,55,115,100,100)
    triangle(115,175,100,130,130,130)
    pop()
def draw():
    global x,y,z,v,y2
    background(255)
    fill(250,255,0)
    ellipse(x,y,z,v)
    translate(0, y2)
    y2 = y2 + 1
    star()
    translate(300,0)
    star()
    if x>=55 and x<=175:
       exit()
    if y>=y2 and y<=120:
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
