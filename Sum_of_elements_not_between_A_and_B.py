n=int(input())
k=list(map(int,input().split()))
a,b=map(int,input().split())
c=sum(k)
h=0
# a=[]
for i in range(len(k)):
    # if(k[i]%2==0):
        
    if(k[i]<a or k[i]>b):
        # 
        h+=k[i]
print(h)        
#     else:
#         a.append(k[i])
# print(*(a+c))        
# if(len(c)==0):
#     print(-1)
# else:
#     print(*(c))
    