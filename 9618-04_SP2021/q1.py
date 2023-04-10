#PART_A

TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]


#PART_B

def InsertionSort(TheData):
	for Count in range(0, len(TheData)):
		DataToInsert = TheData[Count]
		Inserted = 0
		NextValue = Count - 1
		while(NextValue >= 0 and Inserted != 1):
			if(DataToInsert < TheData[NextValue]):
				TheData[NextValue+1] = TheData[NextValue]
				NextValue = NextValue - 1
				TheData[NextValue+1] = DataToInsert
			else:
				Inserted = 1


#PART_C

def PrintArray(TheData):
	for count in range(0, len(TheData)):
		print(TheData[count])


#PART_D-1

print("Before")
PrintArray(TheData)
InsertionSort(TheData)
print("After")
PrintArray(TheData)

#PART_D-2

'''
Before
20
3
4
8
12
99
4
26
4
After
3
4
4
4
8
12
20
26
99
'''


#PART_E-1

def Search(TheData):
	NumberInput = int(input("Enter a whole number: "))
	for count in range(0, len(TheData)):
		if(TheData[count] == NumberInput):
			print("Found")
			return True
	print("Not found")
	return False

Search(TheData)


#PART_E-2

'''
Enter a whole number: 8
Found
-------
Enter a whole number: 9
Not found
'''



