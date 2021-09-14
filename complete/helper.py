# read human player's input
def humanPlayer():
    while True:
        playerOption = input("Coorperate? (Y/N): ")
        if playerOption.upper() == "Y":
            return True
        elif playerOption.upper() == "N":
            return False
        else:
            print("Invalid response \n")
            continue

# human player or human representative
def isHuman():
    while True:
        option = input("1. Human vs Computer\n2. Human Representative (automated) vs Computer \nEnter choice: ")
        if option == '1':
            print()
            return True
        elif option == '2':
            return False
        else:
            print("Invalid response\n")
            continue

# announce the winner
def marker(p1score, p2score):
    if p1score > p2score:
        print("Outcome: You/Human Representative win")
    elif p1score == p2score:
        print("Outcome: Tie")
    else:
        print("Outcome: Computer win")