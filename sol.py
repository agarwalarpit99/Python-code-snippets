n=int(input())
lt=list(map(int,input().split(' ')))
lt2=list(map(int,input().split(' ')))
dic=dict()
lt3=[]
for i in range(n):
    dic[lt[i]]=lt2[i]
for item,quan in dic.items():
    div=quan//item
    lt3.append(div)
print(min(lt3))
    
