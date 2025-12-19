from vpython import *
import math

# 1. 화면 및 물체 설정
scene.background = color.white
ball = sphere(pos=vector(0, 0.1, 0), radius=0.05, color=color.yellow, make_trail=True)
ground = box(pos=vector(0, 0, 0), size=vector(2.5, 0.02, 0.25), color=color.green)

# 2. 그래프 설정
g1 = graph(xtitle="t[s]", ytitle="y[m]")
f1 = gcurve(color=color.blue)

# 3. 물리 상수 및 초기값 설정
g = vector(0, -9.8, 0)
ball.m = 0.05
v0 = 3.5
theta = 73 * (math.pi) / 180
ball.v = v0 * vector(cos(theta), sin(theta), 0)

# 4. 화살표 부착
vscale = 0.1
attach_arrow(ball, "v", scale=vscale, color=color.cyan)

t = 0
dt = 0.01

# 5. 운동 루프 (땅에 닿기 전까지)
# 공의 아랫부분(pos.y - radius)이 바닥의 윗부분(ground.size.y/2)보다 높을 때
while ball.pos.y - ball.radius >= ground.pos.y + ground.size.y/2:
    rate(100)
    
    # 물리 계산
    F = ball.m * g
    a = F / ball.m
    ball.v = ball.v + a * dt
    ball.pos = ball.pos + ball.v * dt
    
    # 시간 및 그래프 업데이트
    t = t + dt
    f1.plot(t, ball.pos.y)
    
    

# 6. 종료 대기 루프 (Q 누르면 종료)
print("운동이 끝났습니다. 'q'를 누르면 창이 닫힙니다.")
while True:
    rate(30)
    keys = keysdown()
    if 'q' in keys:
        print("프로그램을 종료합니다.")
        break