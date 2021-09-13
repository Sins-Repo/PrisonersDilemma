# Agent functions : strategies
import random 

def allCollude():
    return True
    
def allDefect():
    return False
    
def randomDecision():
    return bool(random.randint(0, 1)) # randomly generate either True or False
    
def grudger():
    if grudgerCooperate:
        return True
    else:
        return False

def tft():
    if firstRound:
        return True
    else:
        return humanCooperateHistory[-1] # return the previous move of human player
        
def suspiciousTft():
    if firstRound:
        return False
    else:
        return humanCooperateHistory[-1]
        
def reverseTft():
    if firstRound:
        return False
    else:
        return not humanCooperateHistory[-1] # reverse the previous move of human player

# read human player's input
def humanPlayer():
    while True:
        playerOption = input("Coorperate? (Y/N): ")
        if playerOption.upper() == "Y":
            return True
        elif playerOption.upper() == "N":
            return False
        else:
            print("Not a valid response \n")
            continue

def main(): 
    global firstRound 
    global grudgerCooperate
    global computerScore, humanScore, roundNo
    global humanCooperateHistory

    firstRound = True
    grudgerCooperate = True
    computerScore, humanScore, roundNo = 0, 0, 1
    humanCooperateHistory = []

    strategies = [allCollude, allDefect, randomDecision, grudger, tft, suspiciousTft, reverseTft]

    playerMap = {
        "human" : humanPlayer,
        "computer" : random.choice(strategies)
    }

    while roundNo <= 10:
        # match the agent function names according to the map
        p1Response = playerMap["human"]()
        p2Response = playerMap["computer"]()
        
        # update scores for both players based on the payoff matrix
        if p1Response and p2Response:
            humanScore += 10
            computerScore += 10
        elif p1Response and not p2Response:
            humanScore += 0
            computerScore += 20
        elif not p1Response and p2Response:
            humanScore += 20
            computerScore += 0
        elif not p1Response and not p2Response:
            humanScore += 5
            computerScore += 5
        
        humanCooperateHistory.append(p1Response)
        
        print("\n---------------------------------")
        print(" Decision History & Score Board")
        print("---------------------------------")
        print("Human's decision: ", str(p1Response))
        print("Computer's decision: ", str(p2Response))
        
        print("\nHuman's cumalative score: ", str(humanScore))
        print("Computer's cumulative score: ", str(computerScore))
        print("\n\n")
        
        roundNo += 1
        firstRound = False


    if humanScore > computerScore:
        print("Outcome: You win")
    elif humanScore == computerScore:
        print("Outcome: Tie")
    else:
        print("Outcome: Computer win")
        
    print("Computer's strategy: ", str(playerMap["computer"].__name__))  


if __name__ == "__main__":
	main()