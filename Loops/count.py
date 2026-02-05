# print numbers 1 to 10

i = 1
while i<= 10:
    print(i)
    i +=1

# # print only enven numbers
num = list(range(1,21))
i = 0
while i < len(num):
    j = num[i]
    if j % 2 == 0:
        print(j)
    i += 1

# how to add numbers
add = list(range(1, 100))
i = 0
total = 0
while i< len(add):
  total = total + add[i]
  i += 1
print(total)