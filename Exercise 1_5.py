import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix')
squareBlue = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
squareRed = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])

i =0 
while i < 3:
	squareBlue.draw()
	win.flip()
	core.wait(1)
	win.flip()
	core.wait(.05)
	squareRed.draw()
	win.flip()
	core.wait(1)
	i = i +1
core.wait(1) 
sys.exit()
