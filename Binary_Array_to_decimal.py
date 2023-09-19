n=int(input())
k=list(map(int,input().split()))
for i in range(len(k)):
    k[i]=str(k[i])
a="".join(k)
print(int(a,2))
# c=k.count(0)
# z=k.count(1)
# if(c+z==n):
#     print("True")
# else:
#     print("False")