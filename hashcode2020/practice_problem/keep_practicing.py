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

with open(sys.argv[1], "r") as f: #sys.argv[1]
    line = f.readline()
    m = int(line.split()[0])
    n = int(line.split()[1])

    line = f.readline()
    nums = line.split()
    for i in range(n):
        if int(nums[i]) <= m:
            l.append(int(nums[i]))
    l.sort()
    l.reverse()

log(str(m) + ' ' + str(n))
log(l)
log("###############################################")

##################################################

# TODO function to find next values for holder
# TODO generate holder for each number

max_sum = -1
max_stack = []

hldr_dct = dict()

def find_lower(l, n):
    res = []
    for i in l:
        if i < n:
            res.append(i)
    return res

class holder:

    num = 0
    vb = []
    next = []

    def __init__(self, n, vb, nxt):
        self.num = n
        self.visited_by = vb
        self.next = nxt

def gen_hldr(num):
    global hldr_dct
    val = holder(num, [], find_lower(l, num))
    hldr_dct[num] = val
    
def next_not_visited_by(hldr):
    global hldr_dct
    for i in hldr.next:
        if hldr.num not in hldr_dct[i].visited_by:
            hldr_dct[i].visited_by.append(hldr.num)
            return hldr_dct[i]
    return None

def has_somewhere_to_go(hldr):
    global hldr_dct
    for i in hldr.next:
        if hldr.num not in hldr_dct[i].visited_by:
            return True
    return False

def remove_trace(tmp):
    for i in list(hldr_dct.values()):
        for j in tmp:
            if hldr_dct[j] in i.visited_by:
                i.visited_by.remove(hldr_dct[j])
                log(i.visited_by)

def f1(stack, x):
    global hldr_dct
    global max_sum
    global max_stack

    # log(x.num)
    # log("sum : " + str(sum(stack)))
    # log("next sum : " + str(sum(stack) + x.num))
    # log("stack : " + str(stack))
    log("---------------------")
    if ((sum(stack) + x.num) > m) and sum(stack) <= m:
        if sum(stack) > max_sum:
            max_sum = sum(stack)
            log(max_sum)
            max_stack = stack

    stack.append(x.num)    

    nxt = next_not_visited_by(x)
    if nxt == None:
        if sum(stack) > max_sum and sum(stack) <= m:
            max_sum = sum(stack)
            log(max_sum)
            max_stack = stack
        tmp = [] 
        tmp.append(stack.pop())
        while not has_somewhere_to_go(hldr_dct[stack[-1]]):
            tmp.append(stack.pop()) # this is tmp

            if len(stack) == 0: # if stack is empty then clear visited by of all and return out of recurse
                for i in tmp:
                    hldr_dct[i].visited_by.clear()
                return
            #hldr_dct[tmp].visited_by.clear()
        ### still logical error
        remove_trace(tmp)
        ###
        x = hldr_dct[stack[-1]]
        nxt = next_not_visited_by(x)
        f1(stack, nxt)
    else:
        f1(stack, nxt)

def solution():
    global hldr_dct
    global max_sum
    global max_stack

    # GENERATING HOLDERS FOR EACH NUMBER
    for i in l:
        gen_hldr(i)
    
    # ALGORITHM
    for i in list(hldr_dct.values()):
        stack = []
        stack.append(i.num)
        x = next_not_visited_by(i)
        if x != None:
            f1(stack, x)
        
        #TODO reset visited by of each holder for next round
    
    print(max_sum)
    print(max_stack)

# for i in l:
#     gen_hldr(i)

# stack = [5]

# print(next_not_visited_by(hldr_dct[5]))
# print(hldr_dct[2].visited_by)
# print(has_somewhere_to_go(hldr_dct[stack[-1]]))
# remove_trace([5])
# print(hldr_dct[2].visited_by)
# print(has_somewhere_to_go(hldr_dct[stack[-1]]))
solution()

# i = hldr_dct[8]
# stack = []
# stack.append(i.num)
# x = next_not_visited_by(i)
# if x != None:
#     f1(stack, x)

# log(max_sum)
# log(max_stack)