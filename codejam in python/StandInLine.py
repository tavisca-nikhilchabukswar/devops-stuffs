def Reconstruct(inputList):
    soldiers_standing_position = []
    length = len(inputList)
    for index in range(length-1,0,-1):
        soldiers_standing_position.insert(inputList[index],index+1)

    return soldiers_standing_position
def main():
    print("*****Enter Input with ',' please")
    input_string = input("enter input")
    input_list = list(input_string)
    answer = Reconstruct(input_list)
    for value in answer:
        print(value)


if __name__ == '__main__':
    main()