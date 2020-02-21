DEBUG = True
def log(s):
    if DEBUG:
        print(s)

m = 0
n = 0
l = []

with open("d_quite_big.in", "r") as f:
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

def f1(s_l):
    values = dict()
    _sum = 0
    nums = ""
    i = -1
    for (index, j) in s_l:
        if (_sum + j) > m:
            values[_sum] = nums
            log(str(_sum) + nums)
            break
        _sum += j
        nums += " " + str(index)
        i = index
    values[_sum] = nums
    #log(str(_sum) + nums)
    return values, i

def sol(l, n):
    values = dict()
    for i in range(n, 0, -1):
        _l = list(enumerate(l))
        log(_l)
        s_l = _l[:i]
        log(s_l)
        ret = f1(s_l)
        values.update(ret[0]) 
        log("returned : " + str(ret))
        for j in range(len(s_l)):
            if j < len(s_l) - 2:
                s_l1 = s_l[:j] + s_l[j+1:]
            else:
                s_l1 = s_l[:j]
            log(s_l1)
            ret = f1(s_l1)
            values.update(ret[0]) 
            log("returned : " + str(ret))
            
    log("_________________________________")

    log(values)
    _max = max(values.keys())
    ans_nums = values[_max]
    ans = ans_nums.strip()
    ans = ans.split()
    log("==============================ANS======================")
    print(len(ans))
    print(" ".join(ans))
    
              
            

#SOLUTION END
sol(l, n)