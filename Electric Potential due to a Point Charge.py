import math
from vpython import *

g1 = graph(xtitle="Distance (r)", ytitle="Potential (V)", width=500, height=300)
# 구분을 쉽게 하기 위해 파란 선은 두껍게, 빨간 선은 점선처럼 표현되게 간격을 둡니다.
fv = gcurve(color=color.blue, label="Numerical", width=3)
fc = gcurve(color=color.red, label="Analytical")

k = 9e9
q = 1e-9
rf = 0.5

rq = vector(0, 0, 0)
ro = vector(30, 0, 0)
dr = vector(-0.005, 0, 0)

# [핵심 수정 1] 초기 V를 0이 아니라 시작점(ro=30)의 실제 전위값으로 설정합니다.
V = k * q / mag(ro)

print("시뮬레이션 시작...")

while mag(ro) > rf:
    # [핵심 수정 2] 불필요한 대기 시간을 없애기 위해 속도를 1000으로 올렸습니다.
    rate(1000) 
    
    r = ro - rq
    # 전기장 계산
    E = k * q * norm(r) / mag(r)**2
    
    # 전위 변화량 누적 (dV = -E * dr)
    dV = -dot(E, dr)
    V = V + dV
    
    # [핵심 수정 3] rf(고정값)가 아니라 현재 거리 mag(r)을 나누어야 곡선이 나옵니다.
    Vc = k * q / mag(r)
    
    fv.plot(mag(ro), V)
    fc.plot(mag(r), Vc)
    
    ro = ro + dr

print(f"최종 수치해석 V = {V:.2f} Volts")
print(f"최종 이론값 Vc = {Vc:.2f} Volts")