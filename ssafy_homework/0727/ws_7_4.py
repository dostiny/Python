def fee(time, km):
    rental = (time//10) * 1200  # 시간을 10분으로 나누면 10분당 금액으로 계산이 된다.
    insurance = (time//30) * 525    # 30분당 금액을 계산 / 50분을 빌렸을때는 못함...
    driving = 0
    if km > 100:    # 100km가 넘었을 때
        driving = 170 * km + (85 * (km-100))
    elif km <= 100:    # 100km 이하일 때
        driving = 170 * km
    
    return rental + insurance + driving

print(fee(600, 50))
print(fee(600, 110))