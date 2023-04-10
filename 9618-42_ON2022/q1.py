#PART_A

Jobs = []# global integer, 100 by 2 elements
NumberOfJobs = None # global integer


#PART_B

def Initialise():
	global Jobs
	global NumberOfJobs
	for x in range(0, 100):
		Jobs.append([-1,-1])
	NumberOfJobs = 0


#PART_C

def AddJob(JobNumber, Priority):
	global NumberOfJobs
	global Jobs
	if NumberOfJobs == 100:
		print("Not added")
	else:
		Jobs[NumberOfJobs] = [JobNumber, Priority]
		print("Added")
		NumberOfJobs = NumberOfJobs + 1


#PART_D

Initialise()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)


#PART_E

def InsertionSort():
	global Jobs
	global NumberOfJobs
	for I in range(1, NumberOfJobs):
		Current1 = Jobs[I][0]
		Current2 = Jobs[I][1]
		while I > 0 and Jobs[I-1][1] > Current2:
			Jobs[I][0] = Jobs[I-1][0]
			Jobs[I][1] = Jobs[I-1][1]
			I = I - 1
		Jobs[I][0] = Current1
		Jobs[I][1] = Current2


#PART_F

def PrintArray():
	global Jobs
	global NumberOfJobs
	for X in range(0, NumberOfJobs):
		print(str(Jobs[X][0]), " priority ", str(Jobs[X][1]))



#PART_G-1

InsertionSort()
PrintArray()


#PART_G-2

'''
Added
Added
Added
Added
Added
78  priority  1
33  priority  8
526  priority  9
12  priority  9
12  priority  10

'''
