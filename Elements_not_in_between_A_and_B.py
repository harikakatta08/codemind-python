n=int(input())
k=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
# a=[]
for i in range(len(k)):
    # if(k[i]%2==0):
        
    if(k[i]<a or k[i]>b):
        c.append(k[i])
#     else:
#         a.append(k[i])
# print(*(a+c))        
if(len(c)==0):
    print(-1)
else:
    print(*(c))
    