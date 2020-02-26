from vpython import *
import numpy as np

scene = canvas(width=550, height=550)

GMs = 2 * 10**30 * 6.7 * 10**-20

Sun = sphere(pos=vec(0,0,0),radius=2*10**7,color=color.yellow)
planets = [0,1,2,3]
planets[0] = sphere(pos=vec(7*10**7,0,0),radius=1*10**7,color=color.magenta)
planets[1] = sphere(pos=vec(11*10**7,0,0),radius=1*10**7,color=color.cyan)
planets[2] = sphere(pos=vec(15*10**7,0,0),radius=1*10**7,color=color.blue)        
planets[3] = sphere(pos=vec(25*10**7,0,0),radius=1*10**7,color=color.orange)

Sun.visible = False
for i in range(4):
    planets[i].visible = False

Sun2 = sphere(pos=vec(15*10**7,0,0),radius=1.5*10**7,color=color.yellow)#,make_trail=True)
planets2 = [0,1,2,3]
planets2[0] = sphere(pos=vec(8*10**7,0,0),radius=0.5*10**7,color=color.magenta,make_trail=True)
planets2[1] = sphere(pos=vec(4*10**7,0,0),radius=0.5*10**7,color=color.cyan,make_trail=True)
planets2[2] = sphere(pos=vec(0,0,0),radius=0.5*10**7,color=color.blue,make_trail=True)        
planets2[3] = sphere(pos=vec(-10*10**7,0,0),radius=0.5*10**7,color=color.orange,make_trail=True)

a = [vec(0,0,0),vec(0,0,0),vec(0,0,0),vec(0,0,0)]
v = [vec(0,47,0),vec(0,35,0),vec(0,30,0),vec(0,24,0)]

t = 0
dt = 200
while True:
    rate(50000)
    for i in range(4):
        a[i] = (-1)*(GMs /(mag(planets[i].pos))**3)* planets[i].pos
        v[i] += a[i]*dt
        planets[i].pos += v[i]*dt
        planets2[i].pos = (-1)*planets[i].pos + planets[2].pos
        Sun2.pos = planets[2].pos
    t = t + dt


