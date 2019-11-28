def setup():
    noLoop()
    size(500, 500)
    background(255)
    strokeWeight(30)
    smooth()
    
def draw():
    stroke(20, 100)
    i=0
    while i<7:
        i=i+1
        line(i*50, 200, 150 + (i-1)*50, 300)
        line(i*50 + 100, 200, 50 + (i-1)*50, 300)
