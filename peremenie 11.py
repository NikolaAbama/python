x = 0
mode = 10
def setup():  
    size(600,600)
def draw():
    global x, mode
    background(255)
    if mousePressed == True:
        x = x + mode
        fill(0,0,0)
        ellipse(x,300,80,80)
        if x>=600:
           mode = mode - 10
        if x<=0:
           mode = mode + 10
           
    if mousePressed == False :
        background(255)
