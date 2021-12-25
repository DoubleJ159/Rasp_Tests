'''This code ouputs 1 (Hi/On) to gpio pin 18 for a few seconds then 0 (Low/Off)'''

import time as t
import RPi.GPIO as g

g.setmode(g.BOARD)
g.setup(18, g.OUT)

for i in range (3):
    g.output(18, 1)
    t.sleep(3)
    g.output(18, 0)
    t.sleep(2)
    print("Done ", i)

g.cleanup()
