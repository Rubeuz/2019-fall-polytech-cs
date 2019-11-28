def setup():
    noLoop()
    size(600, 600)
    
def drawMy(myColor):
    fill(myColor)
    rotate(PI/4)
    rect(0, 50, 150, 50)
    rect(50, 0, 50, 150)
    
def draw():
    background(20)
    smooth()
    noStroke()
    
    pushMatrix()
    translate(100, 0)
    drawMy(180)
    popMatrix()
    
    pushMatrix()
    translate(220, 110)
    scale(2)
    drawMy(220)
    popMatrix()
    
    pushMatrix()
    translate(500, 350)
    scale(1.4)
    drawMy(80)
    
