def reverse(lst):
    #first approach
    #lst1 = lst[::-1]
    #print(lst1)
    
    #second
    #lst.reverse()
    #print(lst)
    
    
    #third
    #lst1 = []
    #for i in lst:
        #lst1.insert(0,i)
    #print(lst1)
    
    #fourth 
    left = 0 
    right = len(lst)-1
    
    while (left < right):
        temp = lst[left]
        lst[left]= lst[right]
        lst[right]=temp
        left+=1
        right -=1
    print(lst)
    
inp = [23,4,5,6,78,90]

reverse(inp) 
