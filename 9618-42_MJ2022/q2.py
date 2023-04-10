#PART_A

import random
#main
ArrayData= [[0]*10 for i in range(10)] #integer
for x in range(0, 10):
	for y in range(0,10):
		ArrayData[x][y] = random.randint(1, 100)


#PART_B-2

def printarray(ArrayData):
	for x in range(0, 10):
		for y in range(0, 10):
			print(ArrayData[x][y], " ", end='')
		print("")


print("Before")
printarray(ArrayData)


#PART_B-1

ArrayLength = 10
for X in range(0, ArrayLength):
	for Y in range(0, ArrayLength-1):
		for Z in range(0, ArrayLength - Y - 1):
			if(ArrayData[X][Z] > ArrayData[X][Z+1]):
				TempNumber = ArrayData[X][Z]
				ArrayData[X][Z] = ArrayData[X][Z+1]
				ArrayData[X][Z+1] = TempNumber				
print("After")
printarray(ArrayData)


#PART_B-3

'''
Before
61  36  26  9  17  10  100  91  56  16  
71  68  63  46  9  51  32  5  20  57  
78  52  79  52  20  17  13  7  34  74  
68  74  94  78  52  68  75  28  63  9  
37  59  36  29  42  36  53  36  94  44  
80  25  1  14  84  8  96  71  6  89  
37  35  45  58  46  1  54  15  5  64  
19  64  52  8  92  97  22  8  14  44  
32  63  53  15  18  19  20  41  43  51  
32  56  91  63  15  38  58  64  71  6  
After
9  10  16  17  26  36  56  61  91  100  
5  9  20  32  46  51  57  63  68  71  
7  13  17  20  34  52  52  74  78  79  
9  28  52  63  68  68  74  75  78  94  
29  36  36  36  37  42  44  53  59  94  
1  6  8  14  25  71  80  84  89  96  
1  5  15  35  37  45  46  54  58  64  
8  8  14  19  22  44  52  64  92  97  
15  18  19  20  32  41  43  51  53  63  
6  15  32  38  56  58  63  64  71  91
'''


#PART_C-1

def BinarySearch(SearchArray, Lower, Upper, SearchValue):
	if Upper >= 0:
		Mid = int((Lower + (Upper - 1)) / 2)
		if SearchArray[0][Mid] == SearchValue:
			return Mid
		elif SearchArray[0][Mid] > SearchValue:
			return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
		else:
			return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
	return -1


#PART_C-2

val = int(input())
print(BinarySearch(ArrayData,0,10,val))

val = int(input())
print(BinarySearch(ArrayData,0,10,val))

'''
Before
26  79  25  81  69  45  20  38  16  80  
82  39  49  81  7  13  21  11  28  21  
17  92  25  57  94  1  36  73  45  12  
39  98  96  93  21  48  3  20  21  83  
80  7  22  23  9  72  64  51  74  13  
82  48  42  7  21  49  89  100  8  23  
2  94  96  88  9  66  77  75  24  56  
32  32  58  25  76  86  24  78  89  38  
72  61  67  87  94  23  26  27  45  76  
27  98  57  35  29  29  27  99  98  100  
After
16  20  25  26  38  45  69  79  80  81  
7  11  13  21  21  28  39  49  81  82  
1  12  17  25  36  45  57  73  92  94  
3  20  21  21  39  48  83  93  96  98  
7  9  13  22  23  51  64  72  74  80  
7  8  21  23  42  48  49  82  89  100  
2  9  24  56  66  75  77  88  94  96  
24  25  32  32  38  58  76  78  86  89  
23  26  27  45  61  67  72  76  87  94  
27  27  29  29  35  57  98  98  99  100  
25
2
8
-1
'''

