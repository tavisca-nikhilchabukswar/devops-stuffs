def RackMoves(triangle):
    SolidCorrectPositionCount = 0
    StripsCorrectPositionCount = 0
    TotalSwap = 0
    PositionSetOne = [0,3,5,7,9,10,12]
    PositionSetTwo = [1,2,6,8,11,13,14]
    for position in PositionSetOne:
        if triangle[position] < 8:
            SolidCorrectPositionCount=SolidCorrectPositionCount +1

    for position in PositionSetTwo:
        if triangle[position] > 8:
            StripsCorrectPositionCount = StripsCorrectPositionCount + 1

    if triangle[4] != 8:
        TotalSwap = TotalSwap + 1

    TotalSwap = TotalSwap + GetMinSwipes(SolidCorrectPositionCount,StripsCorrectPositionCount)
    return  TotalSwap

def GetMinSwipes(SolidCorrectPositionCount,StripsCorrectPositionCount):

    SolidToReplace = SolidCorrectPositionCount;
    StripesToReplace = StripsCorrectPositionCount;

    if SolidCorrectPositionCount > 3:
        SolidToReplace = 7 - SolidCorrectPositionCount

    if StripsCorrectPositionCount > 3:
        StripesToReplace = 7 - StripsCorrectPositionCount

    TotalMin = (SolidToReplace + StripesToReplace)/2
    return TotalMin

print("Enter the input:-")
inputNumberList = []
for number in range(15):
    num = int(input("Enter numbers:-"))
    inputNumberList.append(num)
count = RackMoves(inputNumberList)
print("Answer:-",count)




