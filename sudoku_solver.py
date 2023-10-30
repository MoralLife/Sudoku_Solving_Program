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
#str = "900400008 000600197 687915342 470102085 060500730 500760210 005800026 000309801 090200003"
#str = "020784003 800612007 147953060 205400000 001800520 904125300 012348905 000291000 498567030"
#str = "200008000 007000090 900405002 700209005 060000300 000010000 003104500 400080000 000070001"
str = "200798053 357621090 980435012 738249165 160857300 500316200 803164500 400080000 600070001"
'''
추가해야할 기능
+ 어떤 추론에 따라 나온 값인지 알려주기
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
                     if map[row][col] != 0:
                            continue
                     avail = checkCell(avail,row,col,map)
       for row in range(9):
              for col in range(9):
                     if map[row][col] != 0:
                            continue
                     avail = checkArea(avail,row,col,map)
       #print(avail)
       for x in avail:
              if len(avail[x]) == 1:
                     print(f"found = {x}: {avail[x]}")
                     map[x[0]][x[1]] = avail[x].pop()
                     avail[x] = {}
       return map

def checkCell(avail,row,col,map):
       avail[(row,col)] = avail[(row,col)] - (set(map[row]) -  {map[row][col]})
       for i in range(9):
              #print(f"map[{i}][{col}]: {map[i][col]}")
              avail[(row,col)] = avail[(row,col)] - {map[i][col]}
       for r in range((row//3)*3,(row//3)*3+3):
              for c in range(col//3*3,col//3*3+3):
                     avail[(row,col)] = avail[(row,col)] - {map[r][c]}
       return avail

def checkArea(avail,row,col,map):
       #print(f"조건: {row},{col}")
       #print(f"### {avail}")
       if len(avail[(row, col)]) == 1:
              return avail
       rs = avail[(row, col)].copy()
       for i in range(9):
              if i == col:
                     continue
              rs = rs - avail[(row, i)]
       if len(rs) == 1:
              avail[(row, col)] = {rs.pop()}

       cs = avail[(row, col)].copy()
       for i in range(9):
              if i == row:
                     continue
              cs = cs - avail[(i, col)]
       if len(cs) == 1:
              avail[(row, col)] = {cs.pop()}

       rts = avail[(row, col)].copy()
       #print(f"first RTS ({row},{col}) = {rts}")
       for r in range(row // 3 * 3, row // 3 * 3 + 3):
              for c in range(col // 3 * 3, col // 3 * 3 + 3):
                     if map[r][c] != 0:
                            continue
                     if r == row and c == col:
                            continue
                     rts = rts - avail[(r, c)]
                     # print(avail)
                     #print(f"subject ({r},{c}): {rts} 뭘뺐냐면:{avail[(r, c)]}")
       #print(f"After RTS({row},{col}):{rts}")
       if len(rts) == 1:
              avail[(row, col)] = {rts.pop()}
       return avail

def solveAll(map):
       for i in range(44):
              solve(map)


map = makeMap(str)

solveAll(map)
printMap(map)

