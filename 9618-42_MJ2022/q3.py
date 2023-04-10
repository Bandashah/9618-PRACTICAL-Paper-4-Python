#PART_A

class Card:
#Number as Integer
#Colour as string
	def __init__(self, Numberp, Colourp):
		self.__Number = Numberp
		self.__Colour = Colourp

#PART_B

	def GetNumber(self):
		return self.__Number
	def GetColour(self):
		return self.__Colour


#PART_C

CardArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #integer
try:
	Filename = "CardValues.txt"
	File = open(Filename,'r')
	for x in range(0,30):
		NumberRead = int(File.readline())
		ColourRead = File.readline()
		CardArray[x] = Card(NumberRead, ColourRead)
	File.close
except IOError:
	print("Could not find file")


#PART_D

global NumbersChosen

def chooseCard():
	global NumbersChosen
	flagContinue = True
	while flagContinue == True:
		CardSelected = int(input("Select a Card from 1 to 30: "))
		if CardSelected < 1 or CardSelected > 30:
			print("Number must be between 1 and 30")
		elif NumbersChosen[CardSelected - 1] == True:
			print("Already taken")
		else:
			print("Valid")
			flagContinue = False
	NumbersChosen[CardSelected-1] = True
	return CardSelected-1
		

#main

NumbersChosen = [False for i in range(30)]

#PART_E-1

Player1 = [] #of type Card
for x in range(0, 4):
	ReturnNumber = chooseCard()
	Player1.append(CardArray[ReturnNumber])
for x in range(0, 4):
	print(Player1[x].GetColour().strip())
	print(Player1[x].GetNumber())


#PART_E-2

'''
Select a Card from 1 to 30: 1
Valid
Select a Card from 1 to 30: 5
Valid
Select a Card from 1 to 30: 9
Valid
Select a Card from 1 to 30: 10
Valid
red
1
green
9
orange
9
red
10


--------------
Select a Card from 1 to 30: 2
Valid
Select a Card from 1 to 30: 2
Already taken
Select a Card from 1 to 30: 3
Valid
Select a Card from 1 to 30: 4
Valid
Select a Card from 1 to 30: 4
Already taken
Select a Card from 1 to 30: 5
Valid
black
5
white
2
red
4
green
9
'''

