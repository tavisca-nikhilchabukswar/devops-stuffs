def Get(aMinusB,bMinusC,aPlusB,bPlusC):
    blank =[]
    answers_array = get_values_of_ABC(aMinusB,bMinusC,aPlusB,bPlusC)
    if check_for_valid_values(answers_array,aMinusB, bMinusC, aPlusB, bPlusC) == True:
        return answers_array
    else:
        return blank

def get_values_of_ABC(aMinusB,bMinusC,aPlusB,bPlusC):
    value_of_A = (aMinusB + aPlusB)/2
    value_of_B = (bMinusC + bPlusC) / 2;
    value_of_C= (bPlusC - bMinusC) / 2;
    answer = [value_of_A,value_of_B,value_of_C]
    return answer

def check_for_valid_values(AnswersArrya,aMinusB,bMinusC,aPlusB,bPlusC):
    if (AnswersArrya[0] + AnswersArrya[1]) != aPlusB:
        return False
    elif (AnswersArrya[0] - AnswersArrya[1]) != aMinusB:
        return False
    elif (AnswersArrya[1] - AnswersArrya[2]) != bMinusC:
        return False
    elif (AnswersArrya[1] + AnswersArrya[2]) != bPlusC:
        return False
    else: return True

def main():
    aMinusB = int(input("Enter aMinusb"))
    bMinusC = int(input("Enter bMinusC"))
    aPlusB = int(input("Enter aPlusB"))
    bPlusC = int(input("Enter bPlusC"))
    answer = get_values_of_ABC(aMinusB,bMinusC,aPlusB,bPlusC)
    for value in answer:
        print(value)
if __name__ == '__main__':
    main()
