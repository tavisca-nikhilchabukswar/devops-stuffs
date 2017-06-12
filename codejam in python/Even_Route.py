def Is_It_Possible(x, y, wantedParity):
    distance = 0
    parity_list = []
    for index in range(len(x)):
        distance = abs(x[index] + y[index])
        if distance % 2 == 0:
            parity_list.append(0)
        else:
            parity_list.append(1)

    if check_with_wanted_parity(parity_list, wantedParity) == True:
        return "CAN"
    else:
        return "CANNOT"


def check_with_wanted_parity(parity_list, wantedParity):
    for each_parity in parity_list:
        if each_parity == wantedParity:
            return True
    return False


def main():
    xInput = input("Enter X Co-ordinate:- ")
    yInput = input("Enter Y Co-ordinate:- ")
    wantedParity = int(input("Enter Wnated parity:- "))
    result = Is_It_Possible(list(xInput), list(yInput), wantedParity)
    print(result)


if __name__ == "__main__":
    main()