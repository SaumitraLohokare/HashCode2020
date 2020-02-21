import sys

file_name = "a_example.txt"

num_books = 0
num_lib = 0
num_days = 0
score_per_book = dict()
lib_details = dict()

with open(sys.argv[1], "r") as f:
    line = f.readline().split()
    line = list(map(int,line))
    num_books = line[0]
    num_lib = line[1]
    num_days = line[2]
    line = f.readline().split()
    line = list(map(int,line))
    for index, score in enumerate(line):
        score_per_book[index] = score
    for i in range(num_lib):
        line = f.readline().split()
        line = list(map(int,line))
        lib = {"num_book" : line[0], "sign" : line[1], "ship" : line[2], "signed" : False, "sent" : ""}
        line = f.readline().split()
        line = list(map(int,line))
        lib["books"] = line
        lib_details[i] = lib
    
##############################################################

# first sort the books of each library in order of points

def sort_books(lib_no):
    l = lib_details[lib_no]["books"]
    for i in range(len(l) - 1):
        for j in range(i+1, len(l)):
            if score_per_book[l[i]] < score_per_book[l[j]]:
                l[i], l[j] = l[j], l[i]
    lib_details[lib_no]["books"] = l

for i in range(len(lib_details.keys())):
    sort_books(i)

# first solution => ignorre 2 thngs

def _next_not_signed(libs):
    for i in libs:
        if not lib_details[i]["signed"]:
            return i
    return -1

def sort_libs(l):
    for i in range(len(l) - 1):
        for j in range(i+1, len(l)):
            if lib_details[l[i]]["sign"] > lib_details[l[j]]["sign"]:
                l[i], l[j] = l[j], l[i]
    return l

def solution1():
    libs = list(lib_details.keys())#sort_libs(list(lib_details.keys()))

    signing = 0

    sign_order = []

    signed_days = 0
    signed_completed = 0

    for _ in range(num_days):

        libs_sent_for = 0
        for lib in list(lib_details.values()):
            if lib["signed"] and lib["sign"] <= 0:
                libs_sent_for += 1
                for k in range(lib["ship"]):
                    if len(lib["books"]) > 0:    
                        book = lib["books"].pop(0)
                        lib["sent"] += str(book) + str(' ')            

        print("Libraries signed : " + str(signed_completed) + " Libraries sent for : " + str(libs_sent_for))

        if signing <= 0:
            _next = _next_not_signed(libs)
            if _next != -1:
                print(_, end = " : ")
                print (str(_next) + " signing for -> " + str(lib_details[_next]["sign"]))
                lib_details[_next]["signed"] = True
                signed_days += lib_details[_next]["sign"]
                signing = lib_details[_next]["sign"] - 1
                lib_details[_next]["sign"] -= 1
                
        else:
            for lib in list(lib_details.values()):
                if lib["signed"] and lib["sign"] > 0:
                    lib["sign"] -= 1
                    signing -= 1
                    if lib["sign"] == 0:
                        signed_completed += 1
                        print("Added")
                        sign_order.append(str(_next))
                        print ("Completed sign")

    # with open(sys.argv[1].split('.')[0] + '.solution', "w") as sol:
    #     sol.write(str(len(sign_order.strip().split())) + '\n')
    #     for i in list(map(int, sign_order.strip().split())):
    #         if len(lib_details[i]["sent"].strip().split()) > 0:
    #             sol.write(str(i) + ' ' + str(len(lib_details[i]["sent"].strip().split())) + '\n')
    #             sol.write(lib_details[i]["sent"] + '\n')

    print("Signed Days : " + str(signed_days))
    print("Books signed : " + str(signed_completed))

    test = 0
    print(len(sign_order))
    for i in list(map(int, sign_order)):
        if lib_details[i]["sign"] == 0:
            test += 1
        #if len(lib_details[i]["sent"].strip().split()) > 0:
            
            #print(str(i) + ' ' + str(len(lib_details[i]["sent"].strip().split())))
            #print(lib_details[i]["sent"])
    print("signed : " + str(test))


solution1()
