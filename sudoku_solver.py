from collections import defaultdict
# map = [[0,0,7,4,0,0,2,0,3],
#        [0,9,0,0,8,0,0,0,0],
#        [0,0,0,0,0,5,0,0,0],
#        [0,0,0,9,2,0,0,3,7],
#        [0,0,8,0,4,0,1,0,6],
#        [0,0,0,0,5,8,9,0,0],
#        [6,0,0,0,0,3,0,0,8],
#        [0,3,1,6,0,4,7,0,5],
#        [0,4,0,0,7,0,3,0,0]]
#str = "007400203 090080000 000005000 000920037 008040106 000058900 600003008 031604705 040070300"
str = "900400008 000600197 687915342 470102085 060500730 500760210 005800026 000309801 090200003"
'''
추가해야할 기능
avail에 있는 숫자중에, 해당 Rect, Row, Col 중 유일한 가능 숫자를 가지고 있는가?
있다면 그것으로 채우기(그리고 dict 비우기)
+ 종료 조건
'''
def makeMap(str):
       map = []
       for r in str.split():
              t = []
              for c in r:
                     t.append(int(c))
              map.append(t)
       return map

def printMap(map):
       for row in range(0,9):
              if row % 3 == 0:
                     print("-------------------------")
              for col in range(0,9):
                     if col == 0:
                            print("| ",end="")
                     if map[row][col] == 0:
                            print(". ",end="")
                     else:
                            print(f'{map[row][col]} ',end="")
                     if col % 3 == 2:
                            print("| ",end="")
                     if col == 8:
                            print("")
       print("-------------------------")

def solve(map):
       avail = defaultdict(set)
       for row in range(0,9):
              for col in range(0,9):
                     if map[row][col] == 0:
                            avail[(row,col)] = {1,2,3,4,5,6,7,8,9}
       for row in range(0,9):
              for col in range(0,9):
                     avail = checkCell(avail,row,col,map)
       #print(avail)
       for x in avail:
              if len(avail[x]) == 1:
                     print(f"found = {x}: {avail[x]}")
                     map[x[0]][x[1]] = avail[x].pop()
                     avail[x] = {}
       return map
def checkCell(avail,row,col,map):
       avail[(row,col)] = avail[(row,col)] - set(map[row])
       for i in range(0,9):
              #print(f"map[{i}][{col}]: {map[i][col]}")
              avail[(row,col)] = avail[(row,col)] - {map[i][col]}
       for r in range((row//3)*3,(row//3)*3+3):
              for c in range(col//3*3,col//3*3+3):
                     avail[(row,col)] = avail[(row,col)] - {map[r][c]}
       return avail
def solveAll(map):
       for i in range(55):
              solve(map)

map = makeMap(str)

solveAll(map)
printMap(map)
