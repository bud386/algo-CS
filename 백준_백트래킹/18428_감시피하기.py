import sys
input = sys.stdin.readline

N = int(input())
board = [list(input().split()) for _ in range(N)]
teachers = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'T':
            teachers.append((i,j))

def dfs(cnt):    
    if cnt == 3:
        for now in teachers:
            top = now[0] - 1 
            bottom = now[0] + 1
            right = now[1] + 1
            left = now[1] - 1

            while top >= 0:                
                if board[top][now[1]] == 'S':
                    return
                elif board[top][now[1]] == 'O':                    
                    break
                top -= 1

            while bottom < N:
                if board[bottom][now[1]] == 'S':                    
                    return
                elif board[bottom][now[1]] == 'O':                    
                    break
                bottom += 1
                
            while right < N:
                if board[now[0]][right] == 'S':                    
                    return
                elif board[now[0]][right] == 'O':
                    break
                right += 1
            
            while left >= 0:
                if board[now[0]][left] == 'S':                    
                    return
                elif board[now[0]][left] == 'O':
                    break
                left -= 1
        
        print('YES')
        exit()

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                board[i][j] = 'O'                      
                dfs(cnt + 1)
                board[i][j] = 'X'
                    
dfs(0)
print('NO')

########################################################################################################################

import sys

input = sys.stdin.readline

n = int(input())
board = [["O"]*(n+2)]+[["O"]+list(input().split())+["O"] for _ in range(n)]+[["O"]*(n+2)]
teacher = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if board[i][j] == "T":
            teacher.append((i, j))
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
lines = []  # ????????? ??? ??? ?????? ?????? ?????????

for r, c in teacher:
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        line = []
        while board[nr][nc] == "X":  # ???????????? ?????? ????????? ??????
            line.append((nr, nc))
            nr, nc = nr+dr[i], nc+dc[i]
        if board[nr][nc] == "S":  # ????????? ?????? ????????? ???????????? ?????? ???????????? append
            lines.append(line)

lines.sort(key = lambda x: len(x))
count = 0
while lines and count<3:  # ?????? ????????? ????????? ?????? ??????????????? ??????
    now = lines[0]
    if len(now)==0: break  # ?????? ????????? ????????? 0????????? ?????????????????? break
    maxL = []
    for block1 in now:  # ?????? ????????? ?????? ???????????? ????????? ????????? ????????? tmp??? ??????
        tmp = [0]
        for i in range(1, len(lines)): 
            for block2 in lines[i]:
                if block1==block2:
                    tmp.append(i)
                    break
        if len(maxL) < len(tmp):
            maxL = tmp
    for i in maxL[::-1]:  # ?????? ?????? ????????? ????????? ??????
        lines.pop(i)
    count += 1

if lines:
    print("NO")
else: print("YES")