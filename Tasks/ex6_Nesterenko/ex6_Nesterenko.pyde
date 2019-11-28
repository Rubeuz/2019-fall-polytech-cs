eS=5

def setup():
    size(500, 500)
    fill(0)
    strokeWeight(100)
    noLoop()
    
def draw():
    smooth()
    background(100)
    stroke(255)
    strokeWeight(10)
    point(200, 200)
    ellipse(200, 200, eS, eS)
    strokeWeight(30)
    point(300, 200)
    ellipse(300, 200, eS, eS)
    strokeWeight(50)
    point(200, 300)
    ellipse(200, 300, eS, eS)
    strokeWeight(80)
    point(300, 300)
    ellipse(300, 300, eS, eS)
