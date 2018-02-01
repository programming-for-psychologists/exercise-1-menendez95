import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix')
squareBlue = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
squareRed.draw()
win.flip()
core.wait(1)

squareBlue.draw()
win.flip()
core.wait(1) 
sys.exit()
