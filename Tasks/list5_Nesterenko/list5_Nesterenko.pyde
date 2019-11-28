wW = 500
wH = 500
eS = 100
eW = 200
eH = 300

def setup():
    size(wW, wH)
    background(255)
    fill(50, 80)
    strokeWeight(3)
    stroke(100)
    smooth()
    noLoop()
    
def draw():

    ellipse(wW/2, wH/2 - eS/2, eW, eH)
    ellipse(wW/2 - eS/2, wH/2, eW, eH)
    ellipse(wW/2 + eS/2, wH/2, eW, eH)
    ellipse(wW/2, wH/2 + eS/2, eW, eH)
