
D = ["abcbd", "befb", "bgcd", "bde", "abeg", "bgh"]
let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
count = [0, 0, 0, 0, 0, 0, 0, 0]

for i in D:
    consider=[]
    for j in range(len(i)):
        if i[j] in let and i[j] not in consider:
            k=let.index(i[j])
            count[k]=count[k]+1
            consider.append(i[j])

print(count)

P = [.0, .0, .0, .0, .0, .0, .0, .0]
N = len(D)
for i in range(len(count)):
    P[i] = (N-count[i]+0.5)/(count[i]+0.5)

print(P)

q = "ach"
rank = [.0, .0, .0, .0, .0, .0]
for i in range(len(D)):
    temp = 1
    for j in D[i]:
        if j in q:
            temp = temp*P[let.index(j)]
    rank[i] = temp

print(rank)
temp_rank = rank
sorted=[]
high=0
for j in range(6):
    for i in range(len(temp_rank)):
        if(temp_rank[i]>temp_rank[high]):
            high=i
    sorted.append(D[high])
    temp_rank[high]=0

print(sorted)
