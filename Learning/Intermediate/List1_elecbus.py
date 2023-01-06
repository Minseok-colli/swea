#K = 한번 충전으로 최대로 이동하는 정류장, N - 종점 , M = 충전기가 설치된 정류장 번호

T = int(input())
for test_case in range(0,T):
    K,N,M = map(int,input().split())
    M = list(map(int,input().split()))

    now = count = 0
    can_go  = now+K
    charge_station = 0

    while(can_go<N):
        for i in M:
            if now < i <= can_go:
                charge_station = i
            elif can_go < i:
                break
            
        if charge_station == -1:
            count = 0
            break

        now = charge_station
        can_go = now + K
        count += 1
        charge_station = -1
    
    print("#{} {}".format(test_case+1,count))