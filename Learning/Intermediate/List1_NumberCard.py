T = int(input())

for test_case in range(0,T):
    k = int(input())
    num = sorted(list(map(int,input().rstrip())))
    max = 0
    max_num = 0
    
    for i in num:
        if(num.count(i) >= max):
            max = num.count(i)
            if(max_num <= i):
                max_num = i

    print("#{} {} {}".format(test_case+1, max_num, max))