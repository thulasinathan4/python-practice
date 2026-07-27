def mma_lst(mn):    
    minimum=min(mn)
    maximum=max(mn)
    average=sum(mn)/len(mn)
    return minimum,maximum,average
minimum,maximum,average=mma_lst([10,20,30,40])
print('Minimum :',minimum)
print('Maximum :',maximum)
print('Average :',average)