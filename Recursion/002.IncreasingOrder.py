def IncreasingOrder(x):  #10 ,9 ,8 ,7,6,5,4,3,2,1,0
    if x<0:
        return 0
    else:
        # x =10 , 9 1
        IncreasingOrder(x-1)   # 10,9,8,7,6,5,4,3,2,1,0
        print(x)

IncreasingOrder(10)
