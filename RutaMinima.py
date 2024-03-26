#TODO TEST
def main():
    return

def l(D,i,currentSum,n,pi:list):
    if(i==n):
        return GetSum(D,pi)
    elif pi[i]==-1:
        for elem in pi:
            recursions:list=[]
            if(pi[elem]==-1):
                piCopy=pi.copy()
                piCopy[i]=elem
                piCopy[elem]=i
                recursions.append(l(D,i+1,currentSum,piCopy))
            else:continue
            return min(recursions)
    else:
        return l(D,i+1,currentSum,pi)
    
def GetSum(D,pi,n):
    sum=D[pi[n-1]][pi[0]]
    for i in range(n-2):
        sum+=D[pi[i]][pi[i+1]]
    return sum

main()
