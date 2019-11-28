def setup():
    noLoop()
    size(500, 500)
    background(255)
    strokeWeight(30)
    smooth()
    
def draw():
    stroke(20)
    line(50, 200, 150, 300)
    line(2*50, 200, 150+50, 300)
    line(3*50, 200, 150+2*50, 300)
    line(4*50, 200, 150+3*50, 300)    
    line(5*50, 200, 150+4*50, 300)    
    line(6*50, 200, 150+5*50, 300)       
    line(7*50, 200, 150+6*50, 300) 
