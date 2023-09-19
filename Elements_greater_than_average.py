n=int(input())
k=list(map(int,input().split()))
a=sum(k)
c=a//n
h=0
for i in range(n):
    if(k[i]>=c):
        h+=1
print(h)        
#     k[i]=str(k[i])
# a="".join(k)
# print(int(a,2))
# c=k.count(0)
# z=k.count(1)
# if(c+z==n):
#     print("True")
# else:
#     print("False")