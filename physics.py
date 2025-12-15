from vpython import * #opip  install vpython , INCITING TRICKET
import math # sqrt 함수호출법 항상 생각
A= vector(1,-2,1)
B= vector(0.3,4,0)
C=A+B
print("|C|=",mag(C)) # math.sqrt(C.x**2+C.y**2+C.z**2)
print("C hat=",norm(C)) #unit vector C/mag(C)
C=3*A
print("3C=",C)
print(A*B)# CANT INTERPRET
print(dot(A,B)) # DOT PRODOCT
print(cross(A,B))# 벡터사이는 항상 콤마로 찍힌다. CROSS PRODOCT


# A Phyics Problem
# v=v0+at, in acceralation motion with steady speed, a=delta(v1-v0/delta t)
v=0+0.45*1.5
print(v)
# program 
x=0 #m
v=0.45 # m/s
t=0
dt=0.25 #time unit
while(t<1.5):
    x=x+v*dt
    t=t+dt
    print()
print("x=",x,"m")# unit "m"

# Accelerating cart 
x=0
t=0
dt=.1 # 
v=0.45
a=-0.2
while True:# v>=0: 
    v=v+a*dt
    x=x+v*dt
    t=t+dt
    if (v<=0): # v==0 is very dangerous cus computer use float 
        print("object stop")
        break
    

print("x=",x)
print("t=",t)

