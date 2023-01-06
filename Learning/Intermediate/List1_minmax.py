T = int(input())
arr=[]
for test_case in range(0,T):
    N = int(input())
    arr = list(map(int,input().split()))
    print("#{} {}".format(test_case+1,max(arr)-min(arr)))