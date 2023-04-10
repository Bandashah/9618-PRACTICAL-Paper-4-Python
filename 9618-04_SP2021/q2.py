#PART_A

class HiddenBox:
# __BoxName String
# __Creator String
# __DateHidden String
# __GameLocation String
# __LastFinds [10][2] String
# __Active String
	
#PART_B
	def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewLocation):
		self.__BoxName = NewBoxName
		self.__Creator = NewCreator
		self.__DateHidden = NewDateHidden
		self.__GameLocation = NewLocation
		self.__LastFinds = [["" for j in range(0, 2)] for I in range(0, 10)]
		self.__Active = False

#PART_C

	def GetBoxName():
		return self.__BoxName
	def GetLocation():
		return self.__GameLocation

#PART_D-1

TheBoxes = [HiddenBox("","","","") for I in range(0, 10000)]


#PART_D-2

NumBoxes = 0

def NewBox(TheBoxes, NumBoxes):
	BoxName = input("Enter the name of the box")
	Creator = input("Enter the creator’s name")
	DateHidden = input("Enter the date the box was hidden")
	Location = input("Enter the location of the box")
	TheBoxes[NumBoxes] = HiddenBox(BoxName, Creator, DateHidden, Location)
	return(NumBoxes + 1)


#PART_D-3

NumBoxes = NewBox(TheBoxes, NumBoxes)


#PART_E

class PuzzleBox(HiddenBox):
# __PuzzleText String
# __Solution String
	def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewLocation, NewPuzzleText, NewSolution):
		super().__init__(NewBoxName, NewCreator, NewDateHidden, NewLocation)
		self.__PuzzleText = NewPuzzleText
		self.__Solution = NewSolution

