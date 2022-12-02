# Consider telephone book database of N clients. Make use of a hash table implementation 
# to quickly look up client‘s telephone number. Make use of two collision handling 
# techniques and compare them using number of comparisons required to find a set of 
# telephone numbers


tableL = {}
tableQ = {}
totalL=0
totalQ=0

def create(b):   # b is for buckets
    for i in range(b):
        tableL[i] = None
        tableQ[i] = None

def linsert(key, b):
    global totalL
    flag=0
    hash = key % b
    if tableL[hash] == None:
        tableL[hash]=key
    else:
        for i in range (0,b):
            hash = (key+i)%b
            if tableL[hash] == None:
                tableL[hash] = key
                totalL =+ 1
                flag =+ 1
                break
        if flag == 0:
            print("Table full or key not probed ")

def qinsert(key, b):
    global totalQ
    flag=0
    hash = key % b
    if tableQ[hash] == None:
        tableQ[hash]=key
    else:
        for i in range (0,int((b-1)/2)):
            hash = (key+(i*i))%b
            if tableQ[hash] == None:
                tableQ[hash] = key
                totalQ =+ 1
                flag =+ 1
                break
        if flag == 0:
            print("Table full or key not probed ")





def lsearch(key, b):
    flag=0
    hash = key % b
    if tableL[hash] == None:
        print("Key : ",key," is not present! ")
    else:
        for i in range (0,b):
            hash = (key+i)%b
            if tableL[hash] == None:
                print("Key : ", key, " is not present! ")
                flag =+ 1
                break
            elif tableL[hash] == key :
                print("Key : ", key, " is present at location : ",hash)
                flag = + 1
                break

        if flag == 0:
            print("Key : ", key, " is not present! ")

def qsearch(key, b):
    flag=0
    hash = key % b
    if tableQ[hash] == None:
        print("Key : ",key," is not present! ")
    else:
        for i in range (0,int((b-1)/2)):
            hash = (key+(i*i))%b
            if tableQ[hash] == None:
                print("Key : ", key, " is not present! ")
                flag = + 1
                break
            elif tableQ[hash] == key:
                print("Key : ", key, " is present at location : ", hash)
                flag = + 1
                break

        if flag == 0:
            print("Key : ", key, " is not present! ")






def printtable(b):
    print("\nLINEARLY PROBED TABLE : ")
    for i in range(b):
        print(tableL[i],end="|")
    print("\n\nQUADRATICALLY PROBED TABLE : ")
    for i in range(b):
        print(tableQ[i],end="|")
    print("\n")


b = int(input("Enter the table size : "))
create(b)
while(1):
    ch=int(input("ENTER 1 - LP  || 2 - QP || 3 - EXIT : "))

    if ch == 1:
        while(1):
            ch2=int(input("ENTER 1 - INSERT || 2 - SEARCH || 3 - BACK : "))
            if ch2==1:
                if totalL==b:
                    print("Table is already full! ")
                else:
                    key = int(input("Enter the key to be inserted in table : "))
                    linsert(key,b)

            elif ch2==2:
                key = int(input("Enter the key to be searched in table : "))
                lsearch(key,b)

            elif ch2 == 3:
                break
            printtable(b)

    elif ch == 2:
        while(1):
            ch2=int(input("ENTER 1 - INSERT || 2 - SEARCH || 3 - BACK : "))
            if ch2==1:
                if totalQ==b:
                    print("Table is already full! ")
                else:
                    key = int(input("Enter the key to be inserted in table : "))
                    qinsert(key,b)

            elif ch2==2:
                key = int(input("Enter the key to be searched in table : "))
                qsearch(key,b)

            elif ch2 == 3:
                break
            printtable(b)

    elif ch == 3:
        print("EXITING ")
        break
        printtable(b)











