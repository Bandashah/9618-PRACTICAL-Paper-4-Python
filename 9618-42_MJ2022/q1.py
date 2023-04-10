#PART_A

global StackData #integer
global StackPointer
StackData = [0,0,0,0,0,0,0,0,0,0] #integer
StackPointer = 0

#PART_B

def PrintArray():
	global StackData
	global StackPointer
	print(StackPointer)
	for x in range (0, 10):
		print(StackData[x])

#PART_C

def Push(DataToPush):
	global StackData
	global StackPointer
	if StackPointer == 10:
		return False
	else:
		StackData[StackPointer] = DataToPush
		StackPointer = StackPointer + 1
		return True


#PART_D-1

for x in range(0, 11):
	TempNumber = int(input("Enter a number: "))
	if Push(TempNumber) == True:
		print("Stored")
	else:
		print("Stack full")

PrintArray()


#PART_D-2

'''
Enter a number11
Stored
Enter a number12
Stored
Enter a number13
Stored
Enter a number14
Stored
Enter a number15
Stored
Enter a number16
Stored
Enter a number17
Stored
Enter a number18
Stored
Enter a number19
Stored
Enter a number20
Stored
Enter a number21
Stack full
10
11
12
13
14
15
16
17
18
19
20
'''

#PART_E-1

def Pop():
	global StackData
	global StackPointer
	if StackPointer == 0:
		return -1
	else:
		ReturnData = StackData[StackPointer - 1]
		StackPointer = StackPointer - 1
		return ReturnData

print(Pop())
print(Pop())

PrintArray()
