import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix')
squareBlue = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
squareRed = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
squareRed.draw()
win.flip()
core.wait(1)
squareRed.setOri(45)
squareRed.draw()
win.flip()
core.wait(1) 
sys.exit()
