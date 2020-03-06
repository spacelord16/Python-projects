from graphics import *
win=GraphWin()

pt=Point(100,50)
pt.draw(win)

cir=Circle(pt,25)
cir.draw(win)

cir.setOutline('red')
cir.setFill('blue')

line=Line(pt,Point(150,100))
line.draw(win)

rect=Rectangle(Point(20,10),pt)
rect.draw(win)

line.move(10,40)

win.close()

print('cir',cir)
print('line',line)
print('rect',rect)