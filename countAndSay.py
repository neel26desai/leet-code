s="1211"
ans=''
digit = s[0]
count=1
for i in range(1,len(s)):
    if s[i]==digit:
        #increase the count
        count+=1
    else:
        #we can across a new digit, e all the previous count and digit to our ans string after which we will update the digit to the new value of digit and count back to 1
        ans=ans+str(count)+digit
        #update value for digit and count
        digit = s[i]
        count=1
#the last digit and its count wont be added in the for loop, so we add them 
ans=ans+str(count)+digit
print(ans)
