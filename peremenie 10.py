def setup():
    size(600,600)
    background(0,0,0)
def draw():

    if mousePressed == False:
        fill(4,134,239)
        ellipse(random(0,600),random(0,600),10,10)
    if mousePressed == True:
       background(0,0,0)
