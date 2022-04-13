def setup():
    size(600,600)
    background(255)
def draw():
    push()
    fill(random(0,255),random(0,255),random(0,255))
    rect(mouseX,mouseY,80,80)
    ellipse(mouseX,mouseY,80,80)
    pop()
