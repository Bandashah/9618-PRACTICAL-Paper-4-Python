#PART_A-1

class Card:
#Number as integer
#Colour as string
	def __init__(self, Number1, Colour1):
		self.__Number = Number1
		self.__Colour = Colour1

#PART_A-2

	def GetNumber(self):
		return self.__Number
	def GetColour(self):
		return self.__Colour


#PART_A-3

OneRed = Card(1, "red")
TwoRed = Card(2, "red")
ThreeRed = Card(3, "red")
FourRed = Card(4, "red")
FiveRed = Card(5, "red")

OneBlue = Card(1, "blue")
TwoBlue = Card(2, "blue")
ThreeBlue = Card(3, "blue")
FourBlue = Card(4, "blue")
FiveBlue = Card(5, "blue")

OneYellow = Card(1, "yellow")
TwoYellow = Card(2, "yellow")
ThreeYellow = Card(3, "yellow")
FourYellow = Card(4, "yellow")
FiveYellow = Card(5, "yellow")


#PART_B-1

class Hand:
	#Cards[10] as Card
	#FirstCard as integer
	#NumberCards as integer
	def __init__(self, Card1, Card2, Card3, Card4, Card5):
		self.__Cards = []
		self.__Cards.append(Card1)
		self.__Cards.append(Card2)
		self.__Cards.append(Card3)
		self.__Cards.append(Card4)
		self.__Cards.append(Card5)
		self.__FirstCard = 0
		self.__NumberCards = 5

#PART_B-2

	def GetCard(self, Position):
		return self.__Cards[Position]


#PART_B-3

Player1 = Hand(OneRed, TwoRed, ThreeRed, FourRed, OneYellow)
Player2 = Hand(TwoYellow, ThreeYellow, FourYellow, FiveYellow, OneBlue)



#PART_C-1

def CalculateValue(Player):
	Score = 0
	for Count in range(0, 4):
		CardGot = Player.GetCard(Count)
		Score = Score + CardGot.GetNumber()
		Colour = CardGot.GetColour()
		if Colour == "red":
			Score = Score + 5
		elif Colour == "blue":
			Score = Score + 10
		else:
			Score = Score + 15
	return Score


#PART_C-2

Player1score = CalculateValue(Player1)
Player2score = CalculateValue(Player2)
if Player1score > Player2score:
	print("Player 1 wins")
elif Player1score < Player2score:
	print("Player 2 wins")
else:
	print("It's a draw")

