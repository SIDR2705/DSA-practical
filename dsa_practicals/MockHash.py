tableL={}
tableQ={}
totalL=0
totalQ=0

def create(b):

	for i in range (b):

		tableL[i] = None
		tableQ[i] = None

def linsert(key,b):

	global totalL
	flag=0
	hash=key%b 
	if tableL[hash]== None:
		tableL[hash]=key
	else:
		for i in range (0,b):
			hash=(key+i)%b 
			if tableL[hash]== None:
				tableL[hash]=key
				totalL=+1
				flag=+1
				break

		if flag==0:
			print("table is full ")
		


def qinsert(key,b):

	global totalQ
	flag=0
	hash=key%b 
	if tableQ[hash]== None:
		tableQ[hash]=key
	else:
	for i in range (0,int (b-1)/2):
		hash=(key+(i*i))%b 
		if tableQ[hash]== None:
			tableQ[hash]=key
			totalQ=+1
			flag=+1
			break

		if flag==0:
			print("table is full ")
		


def lsearch (key,b):
 
	flag=0
	hash=key%b 
	if tableL[hash]== None:
		print(" key is not present ")

	else:
		for i in range (0,b):
			hash=(key+i)%b 
		if tableL[hash]== None:
			print(" key is not present ")
			flag=+1
			break
		elif
			tableL[hash]=key:
			print(" Key ", key," is present at loccation ",hash)
			flag=+1
			break


	if flag==0:
	print("table is full ")



def qsearch (key,b):
 
	flag=0
	hash=key%b 
	if tableQ[hash]== None:
		print(" key is not present ")

	else:
		for i in range (0,int((b-1)/2):
		hash=(key+i)%b 
		if tableQ[hash]== None:
			print(" key is not present ")
			flag=+1
			break

		elif
			tableQ[hash]=key:
			print(" Key ", key," is present at loccation ",hash)
			flag=+1
			break


	if flag==0:
		print("table is full ")

def printtable(b):
print("Linearyly Probed table")
	for i in range (0,b)
	print(tableL[i],end="|")
print("Quadratic Probed table")
	for i in range (0,b)
	print(tableQ[i],end="|")


b=int(input("Enter the size of the table"))
create(b)
while(1):
	 ch=int(input("|| 1. LP || 2.QP || 3. EXIT || :"))

	 
	 	if ch==1 :
	 		while(1):
	 			ch1==int(input("|| 1.INSERT || 2.SEARCH || 3. BACK || :"))
	 			if ch==1:
	 				if totalL==b
	 					print("Table is full.")
		 	else 
		 		key=int(input("Enter the key to be inserted :"))
		 		linsert(key,b)
		 	break

		 	elif ch==2 :
		 		key=int(input("Enter the key to be Searched :"))
		 		lsearch(key,b)

		 	elif ch==3:
		 	break
		 	printtable(b)

		 elif ch==2:
			 	while(1):
		 		ch1==int(input("|| 1.INSERT || 2.SEARCH || 3. BACK || :"))
			 		if ch==1:
			 			if totalQ==b
			 		print("Table is full.")
			 	else 
				 	key=int(input("Enter the key to be inserted :"))
				 	qinsert(key,b)
				 	break

			 	elif ch==2 :
				 	key=int(input("Enter the key to be Searched :"))
				 	qsearch(key,b)

			 	elif ch==3:
				 	break
				 	printtable(b)

		 elif ch==3:
			 	break
			 	printtable(b)
