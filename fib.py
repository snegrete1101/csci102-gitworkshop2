#Sebastian Negrete-Alamillo
#CSCI 102 - Section E
#Git Workshop 2

fibs = [1,1]

for i in range(1,99):
    f = fibs[i-1] + fibs[i]
    fibs.append(f)

for i in fibs:
    print(i)
