a=[1,2,3,4,5,6,8]
target=7
ans =-1
l,r = 0 ,len(a)-1
mid = (l+r)//2
while l<=r:
    if target<a[mid]:
        