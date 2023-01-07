t = input()

for testcase in range(t):
    #1 사각형 갯수 입력
    n = input()
    box = purple = []
    #2 사각형 좌표입력
    for i in range(n):
        box[i] = list(map(int,input().split()))
    
    #3 사각형들의 좌표를 비교하며 색이 교차되면 리스트에 저장
    
   for y in range(len(box)):
        for x in range(len(box[y])):
            for z in range(2):

#4 리스트 개수 출력