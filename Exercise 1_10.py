import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix')
squareBlue = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
squareRed = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
squareBlue.draw()
win.flip()
core.wait(1)

i= 0
while i < 40000:
	if event.getKeys(['left']):
		squareBlue.size += [10,0]
		squareBlue.draw()
		win.flip()
		i = i + 1
	if event.getKeys(['right']):
		squareBlue.size += [-10,0]
		squareBlue.draw()
		win.flip()
		i = i + 1
	i = i + 1
	

win.flip()
core.wait(1) 
sys.exit()
