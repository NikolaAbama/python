x = 5
y = 5
mode = 1
def setup():
    size(600,600)
def draw():
    global x, y, mode
    background(255)
    fill(random(0,255),random(0,255),random(0,255))
    rect(300,200,x,y)
    x = x + mode
    y = y + mode
    if x>=80 and y>=80:
        mode = -1
    if x<=5 and y<=5:
        mode = 1
