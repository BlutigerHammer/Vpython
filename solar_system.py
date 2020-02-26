from vpython import *
import numpy as np

scene = canvas(width=550, height=550)

GMs = 2 * 10**30 * 6.7 * 10**-20 

Sun = sphere(pos=vec(0,0,0),radius=2*10**7,color=color.yellow)

planets = [0,1,2,3]

planets[0] = sphere(pos=vec(7*10**7,0,0),radius=1*10**7,color=color.magenta,make_trail=True)
planets[1] = sphere(pos=vec(11*10**7,0,0),radius=1*10**7,color=color.cyan,make_trail=True)
planets[2] = sphere(pos=vec(15*10**7,0,0),radius=1*10**7,color=color.blue,make_trail=True)        
planets[3] = sphere(pos=vec(25*10**7,0,0),radius=1*10**7,color=color.orange,make_trail=True)


a = [vec(0,0,0),vec(0,0,0),vec(0,0,0),vec(0,0,0)]
v = [vec(0,47,0),vec(0,35,0),vec(0,30,0),vec(0,24,0)]
    

t = 0
dt = 200
while True:
    rate(15000)
    for i in range(4):
        a[i] = (-1)*(GMs /(abs(mag(planets[i].pos)))**3)* planets[i].pos
        v[i] += a[i]*dt
        planets[i].pos += v[i]*dt
    t = t + dt


