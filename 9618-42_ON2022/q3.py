#PART_A

Queue = [-1 for I in range(100)] #Integer
HeadPointer = -1
TailPointer = 0

#PART_B

def Enqueue(Data):
	global Queue
	global TailPointer
	global HeadPointer
	if(TailPointer < 100):
		if HeadPointer == -1:
			HeadPointer = 0
		Queue[TailPointer] = Data
		TailPointer = TailPointer + 1
		return True
	return False



#PART_C

Success = False
for Count in range(1, 21):
	Success = Enqueue(Count)
if(Success == False):
	print("Unsuccessful")
else:
	print("Successful")


#PART_D

def RecursiveOutput(Start):
	if(Start == 0):
		return Queue[Start]
	else:
		return Queue[Start] + RecursiveOutput(Start - 1)

#PART_E-1

print(str(RecursiveOutput(TailPointer - 1)))


#PART_E-2

'''
Successful
210

'''
