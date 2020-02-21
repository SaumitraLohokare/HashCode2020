import sys
from itertools import combinations

DEBUG = False
if sys.argv[2] == 'debug':
    DEBUG = True
def log(s):
    if DEBUG:
        print(s)

m = 0
n = 0
l = []

with open(sys.argv[1], "r") as f:
    #global m
    #global n
    line = f.readline()
    m = int(line.split()[0])
    n = int(line.split()[1])

    line = f.readline()
    nums = line.split()
    for i in range(n):
        if int(nums[i]) <= m:
            l.append(int(nums[i]))
    l.sort()


# INPUT END
log(str(m) + ' ' + str(n))
log(l)

#SOLUTION START

def solution():
    com = []
    for i in range(1, len(l) + 1):
        com.append(list(combinations(l, i)))
    
    with open("combinations.txt", "w") as f:
        for i in com:
            for j in i:
                f.write(str(list(j)) + "\n")
        f.write("...")
    

    _max = 0
    _max_nums = list()

    with open("combinations.txt", "r") as f:
        line = f.readline()
        while line != "...":
            line = line[1:-2]
            t = line.split(", ")
            temp = [int(x) for x in t]
            
            s = sum(temp)
            if s <= m:
                if s > _max:
                    _max = s
                    _max_nums = t
                if s == m:
                    continue
            
            line = f.readline()
            

    # for i in com:
    #     for j in i:
    #         if sum(j) <= m and sum(j) > _max:
    #             _max = sum(j)
    #             _max_nums = list(j)
    
    log("________________________________________")
    with open("ans_"+sys.argv[1], "w") as f:
        f.write(str(len(_max_nums)) + "\n")
        res = map(lambda x: str(x), _max_nums)
        f.write(" ".join(res))

solution()