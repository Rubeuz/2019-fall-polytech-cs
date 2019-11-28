wW = 600
wH = 600
eS = 200

def setup():
    size(wW, wH)
    background(255)
    fill(50, 80)
    strokeWeight(3)
    stroke(100)
    smooth()
    noLoop()
    
def draw():

    ellipse(wW/2, wH/2 - eS/2, eS, eS)
    ellipse(wW/2 - eS/2, wH/2, eS, eS)
    ellipse(wW/2 + eS/2, wH/2, eS, eS)
    ellipse(wW/2, wH/2 + eS/2, eS, eS)
