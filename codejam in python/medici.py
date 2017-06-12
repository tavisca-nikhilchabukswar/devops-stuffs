def winner(fame, fortune, secrets):
    weak_category_of_each_player = []
    length = len(fame)
    for index in range(length):
        weak_category_of_each_player.append(find_minimum_category_player(fame[index], fortune[index], secrets[index]))

    weak_category_of_each_player.sort()
    max_in_weak_category = weak_category_of_each_player[2]
    count = 0

    for weak_category in weak_category_of_each_player:
        if weak_category == max_in_weak_category:
            count = count + 1
    if count > 1:
        return -1
    else:
        return weak_category_of_each_player.index(max_in_weak_category)


def find_minimum_category_player(fame,fortune,secrets):
    if fame <= fortune and fame <= secrets:
        return fame
    elif fortune <= fame and fortune <= secrets:
        return fortune
    else: return secrets

def main():
    fame = input("Enter Fame:- ")
    fortune = input("Enter Fortune:- ")
    secrets = input("Enter Secrets:- ")
    result = winner(list(fame),list(fortune),list(secrets))
    print (result)

if __name__ == '__main__':
    main()