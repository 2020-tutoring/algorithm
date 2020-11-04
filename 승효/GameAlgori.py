n,m=map(int,input().split())
a,b,d=map(int,input().split())
count=1
confirm=0 #네 방향 모두 가본곳이거나 바다인 경우를 확인
array=[]
for _ in range(n):
  array.append(list(map(int,input().split())))
array[a][b]=2 #이미 방문한 곳은 2로 변환
direction=[(-1,0),(0,1),(1,0),(0,-1)]#북,동,남,서

while(1):
    d=(d-1)%4 #서쪽을 바라봄
    next_a=a+direction[d][0]
    next_b=b+direction[d][1]
    if(array[next_a][next_b]==0): #안가본 육지
      a,b=next_a,next_b
      count+=1
      array[a][b]=2 #가본 곳은 2로 변환
      confirm=0
      continue
    confirm+=1 #가본곳이나 바다인경우
    if(confirm>=4): #네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우
      d=(d-1)%4
      behind_d=(d-2)%4
      behind_a=a+direction[behind_d][0]
      behind_b=b+direction[behind_d][1]
      if(array[behind_a][behind_b]==2): #뒤쪽 방향이 가본 칸인 경우
        a,b=behind_a,behind_b
        confirm=0
        continue
      else: #뒤쪽 칸이 바다칸인 경우
        break
print(count)
    