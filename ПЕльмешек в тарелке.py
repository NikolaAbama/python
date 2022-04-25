x = 300
y = 200
def setup():
    size(600,400)
def draw():
    global x, y 
    background(255)
    #кнопка прямоугольная
    fill(0)
    rect(500,320,100,80)
    fill(255)
    rect(400,320,100,80)
    fill(255,0,0)
    rect(300,320,100,80)
    fill(0,255,57)
    ellipse(x,y,80,80)
def mouseClicked():
    global x, y
    if mouseX>500 and mouseX<500 + 100 and mouseY>320 and mouseY<320 + 80:
       x = x + 10
    if mouseX>400 and mouseX<400 + 100 and mouseY>320 and mouseY<320 + 80:
       x = x - 10
    if mouseX>300 and mouseX<300 + 100 and mouseY>320 and mouseY<320 + 80:
       y = y + 10
