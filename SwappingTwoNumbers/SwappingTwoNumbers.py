def swapTwo(lst):
    if len(lst)>=2:
        lst = lst[-1:]+ lst[1:-1]+lst[:1]
        print(lst)
inp = [23,4,5,6,78,90]
swapTwo(inp)