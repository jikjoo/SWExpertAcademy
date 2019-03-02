for T in range(10):
    N=int(input('\n'))   #Test Case Number
    buildings = [int]  # 5 * int array
    cnt = 0
    building_text = str(input(''))
    buildings = building_text.split(" ")
    for n in range(N-2):
        if n < 2 : continue
        b0 = int(buildings[n])-int(buildings[n-2])
        b1 = int(buildings[n])-int(buildings[n-1])
        b2 = int(buildings[n])-int(buildings[n+1])
        b3 = int(buildings[n])-int(buildings[n+2])
        if b0>0 and b1>0 and b2>0 and b3>0:
            cnt += min([b0,b1,b2,b3])
    print("#"+str(T+1)+" "+str(cnt))
    buildings=[]