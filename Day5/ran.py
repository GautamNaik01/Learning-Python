from random import randint

# k = random.randint(2,100)
# print(k)

avengers = ["Hulk", "Thor", "Iron Man"]
l = len(avengers)
k = randint(0,l-1)
print(avengers[k])
s=""
for i in avengers[k]:
    if i == ' ' or i=='a' or i=='o'or i=='e' or i=='i' or i=='u':
        s+=i
        s+=" "
        continue
    s+="_ "
print(s)