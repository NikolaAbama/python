bg = 0
x = 0
def setup():
    size(600,400)
def draw():
    global bg, x
    background(bg)    
    #кнопка прямоугольная
    fill(255)
    # левый верхний угол 250 150, размеры 100 на 50
    rect(250,150,100,50)# x от 250 до 250+100, y от 150 до 150+50
    fill(0,0,0)
    textSize(50)
    text(x,285,200)
def mouseClicked():
    global bg, x
    # если прямоугольная кнопка нажата
    
    if mouseX>250 and mouseX<350 and mouseY>150 and mouseY<200:
       x = x + 1 
       bg = 255
