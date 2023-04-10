#PART_A

class Picture:
	def __init__(self, DescriptionP, WidthSizeP, HeightSizeP, FrameColourP):
		self.__Description = DescriptionP # string
		self.__Width = int(WidthSizeP) #integer
		self.__Height = int(HeightSizeP) #integer
		self.__FrameColour = FrameColourP #string

#PART_B

	def GetDescription(self):
		return self.__Description
	def GetWidth(self):
		return self.__Width
	def GetHeight(self):
		return self.__Height
	def GetColour(self):
		return self.__FrameColour


#PART_C

	def SetDescription(self, DescriptionP):
		self.__Description = DescriptionP


#PART_D

PictureArray = []
for i in range(100):
	PictureArray.append(Picture("",0,0,""))


#PART_E

def ReadData(PictureArray):
	Filename = "Pictures.txt"
	Counter = 0
	try:
		File = open(Filename,"r")
		Description = (File.readline()).strip().lower()
		while(Description != ""):
			Width = int((File.readline()).strip())
			Height = int((File.readline()).strip())
			Frame = ((File.readline()).strip()).lower()
			PictureArray[Counter] = Picture(Description, Width, Height, Frame)
			Description =((File.readline()).strip()).lower()
			Counter = Counter + 1
		File.close()
	except IOError:
		print("Could not find File")
	return Counter, PictureArray


#PART_F

NumberPicturesInArray, PictureArray = ReadData(PictureArray)


#PART_G

FrameColour = input("Input the Frame colour: ").lower()
MaxWidth = int(input("Input the Maximum Width: "))
MaxHeight = int(input("Input the Maximum Height: "))
print("Matches Frames shown")
for Z in range(0, NumberPicturesInArray):
	if PictureArray[Z].GetColour() == FrameColour:
		if(PictureArray[Z].GetWidth() <= MaxWidth):
			if (PictureArray[Z].GetHeight() <= MaxHeight):
				print(PictureArray[Z].GetDescription(), " " , str(PictureArray[Z].GetWidth()), " ", str(PictureArray[Z].GetHeight()))



#PART_H

'''
Input the Frame colour: BLACK
Input the Maximum Width: 100
Input the Maximum Height: 100
Matches Frames shown
flowers   45   50
people   20   20
landscape   30   45
landscape   25   37
people   50   40

-------------------
Input the Frame colour: silver
Input the Maximum Width: 25
Input the Maximum Height: 25
Matches Frames shown

'''

