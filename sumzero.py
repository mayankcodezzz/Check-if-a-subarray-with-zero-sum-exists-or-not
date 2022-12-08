# check if a sublist with zero-sum is present in a given list or not
def zerosum(list):
    s=set()
    s.add(0)
    # {0},{0,4},{0,4,-2},{0,4,-2,1},{0,4,-2,1}
    sum=0
    for i in list:
        sum=sum+i
        if sum in s:
            return True
        s.add(sum)
    return False


list=[4, -6, 3, -1, 4, 2, 7]
if zerosum(list):
    print("sublist exists")
else:
    print("sublist does not exists")
