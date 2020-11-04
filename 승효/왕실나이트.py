#내 아이디어
location=input()
r=int(location[1])
c=int(ord(location[0]))-int(ord('a'))+1
move=[[-2,-1],[-2,1],[2,1],[2,-1],[-1,-2],[-1,2],[1,-2],[1,2]]
count=0
for moves in move:
  new_r=r+moves[0]
  new_c=c+moves[1]
  if(new_r>8 or new_r<1 or new_c>8 or new_c<1):
    continue
  count=count+1
print(count)

#질문: 3행에서 int괄호를 해주고 안해주고의 차이
