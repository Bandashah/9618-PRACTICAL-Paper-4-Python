#PART_A

class Balloon:
#Health as integer
#Colour as string
#DefenceItem as string
	def __init__(self, PDefenceItem, PColour):
		self.__Health = 100
		self.__Colour = PColour
		self.__DefenceItem = PDefenceItem

#PART_B
	def GetDefenceItem(self):
		return self.__DefenceItem

#PART_C
	def ChangeHealth(self, Change):
		self.__Health = self.__Health + Change

#PART_D

	def CheckHealth(self):
		if self.__Health <= 0:
			return True
		else:
			return False


#PART_E

Method = input("Enter balloon defence method: ")
Colour = input("Enter the balloon colour: ")
Balloon1 = Balloon(Method, Colour)


#PART_F

def Defend(MyBalloon):
	Strength = int(input("Enter the strength of opponent"))
	MyBalloon.ChangeHealth(-Strength)
	print("You defended with ", str(MyBalloon.GetDefenceItem()))
	if(MyBalloon.CheckHealth() == True):
		print("Defence failed")
	else:
		print("Defence succeeded")
	return MyBalloon


#PART_G-1
Balloon1 = Defend(Balloon1)



#PART_G-2

'''
Enter balloon defence method: shield
Enter the balloon colour: red
Enter the strength of opponent50
You defended with  shield
Defence succeeded

'''