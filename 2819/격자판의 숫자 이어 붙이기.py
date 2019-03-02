serials = []
def moveSquare(serial, x, y, cnt, square):
    global serials
    if cnt == 6 : 
        serials.append(serial)
        return
    else:
        # x+1
        if x+1 < 4 :
            moveSquare(serial+square[x+1][y],x+1, y, cnt+1, square)
        # x-1
        if x > 0 :
            moveSquare(serial+square[x-1][y], x-1, y, cnt+1, square)
        # y+1
        if y+1 < 4 :
            moveSquare(serial+square[x][y+1], x, y+1, cnt+1, square)
        # y-1
        if y > 0:
            moveSquare(serial+square[x][y-1], x, y-1, cnt+1, square)

T = int(input(''))
for test_case in range(T):
    square=[]
    for i in range(4):  # 격자 입력 받기
        line = str(input()).strip().split(' ')
        square.append([line[j] for j in range(4)])
    for i in range(4):
        for j in range(4):
            moveSquare(square[i][j],i,j,0,square)
    serials = [i for i in set(serials)]
    result = serials.__len__()
    serials.clear()
    print('#'+str(test_case+1)+" "+str(result))
