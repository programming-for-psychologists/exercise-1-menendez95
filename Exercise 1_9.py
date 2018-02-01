import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix')
squareBlue = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
squareRed = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
squareRed.draw()
win.flip()
core.wait(1)
keys = event.getKeys()

i = 0
while keys == event.getKeys(['s']) and i < 60:
	squareRed.ori += 6
	squareRed.draw()
	win.flip()
	i = i + 1
event.waitKeys(['r'])
while i < 60:
	squareRed.ori += 6
	squareRed.draw()
	win.flip()
	i = i + 1	
core.wait(1)
win.flip()
core.wait(1) 
sys.exit()
