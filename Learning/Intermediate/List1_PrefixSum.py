T = int(input())

for test_case in range(T):
    N,M = map(int,input().split())
    num = list(map(int,input().split()))
    Sum_list = []

    for i in range(N-M+1):
        result = 0
        for j in range(i,i+M):
            result += num[j]
        
        Sum_list.append(result)

    print("#{} {}".format(test_case+1, max(Sum_list)-min(Sum_list)))