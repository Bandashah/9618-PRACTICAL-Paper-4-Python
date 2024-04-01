#9618_w23_41_q3

class Character:
	#self.XPosition integer
	#self.YPosition integer
	#self.Name string
	def	__init__(self, XPositionP, YPositionP, NameP):
		self.XPosition = XPositionP
		self.YPosition = YPositionP
		self.Name = NameP
	
	def GetXPosition(self):
		return self. XPosition
	
	def GetYPosition(self):
		return self. YPosition
	
	def SetXPosition(self, Value):
		self. XPosition = self. XPosition + Value
		if(self.XPosition > 10000):
			self.XPosition = 10000
		elif self.XPosition < 0:
			self.XPosition = 0
	
	def SetYPosition(self, Value):
		self.YPosition = self.YPosition + Value
		if(self.YPosition > 10000):
			self.YPosition = 10000
		elif self.YPosition < 0:
			self.YPosition = 0

	def Move(self, Direction):
		if(Direction == "up"):
			self.SetYPosition(10)
		elif(Direction == "down"):
			self.SetYPosition(-10)
		elif(Direction == "right"):
			self.SetXPosition(10)
		else:
			self.SetXPosition(-10)


class BikeCharacter(Character):
	def __init__(self, XPositionP, YPositionP, NameP):
		super().__init__(XPositionP, YPositionP, NameP)

	def Move(self, Direction):
		if(Direction == "up"):
			super().SetYPosition(20)
		elif(Direction == "down"):
			super().SetYPosition(-20)
		elif(Direction == "right"):
			super().SetXPosition(20)
		else:
			super().SetXPosition(-20)


Jack = Character(50, 50, "Jack")

Karla = BikeCharacter(100, 50, "Karla")


CharacterToMove = input("Would you like to move Jack or Karla?").lower()
while CharacterToMove != "jack" and CharacterToMove != "karla":
	CharacterToMove = input("Invalid try again")

Direction = input("Which direction? Up, down, left or right?")
while Direction != "up" and Direction != "down" and Direction != "left" and Direction != "right":
	Direction = input("Invalid try again")

if CharacterToMove == "jack":
	Jack.Move(Direction)
	print("Jack's new position is X =", Jack.GetXPosition(), "Y =", Jack.GetYPosition())
else:
	Karla.Move(Direction)
	print("Karla's new position is X =", Karla.GetXPosition(), "Y =", Karla.GetYPosition())