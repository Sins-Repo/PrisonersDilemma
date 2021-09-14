import random 
from helper import *

# Agent functions : strategies (Computer & Human Representative)
def allCollude():
    return True
    
def allDefect():
    return False
    
def randomDecision():
    return bool(random.randint(0, 1)) # randomly generate either True or False

# Agent functions : strategies (Computer ONLY)
def grudger():
    if p2grudgerCooperate:
        return True
    else:
        return False

def tft():
    if firstRound:
        return True
    else:
        return p1coopHistory[-1]     # return the previous move of human player / human representative
        
def suspiciousTft():
    if firstRound:
        return False
    else:
        return p1coopHistory[-1]
        
def reverseTft():
    if firstRound:
        return False
    else:
        return not p1coopHistory[-1]  # reverse the previous move of human player / human representative


# Agent functions : strategies (Human Representative ONLY)       
def grudgerRep():
    if p1grudgerCooperate:
        return True
    else:
        return False
        
def tftRep():
    if firstRound:
        return True
    else:
        return p2coopHistory[-1]
        
def suspiciousTftRep():
    if firstRound:
        return False
    else:
        return p2coopHistory[-1]
        
def reverseTftRep():
    if firstRound:
        return False
    else:
        return not p2coopHistory[-1]        

# main function
def main(): 
    global firstRound 
    global p1grudgerCooperate, p2grudgerCooperate
    global p1score, p2score, roundNo
    global p1coopHistory, p2coopHistory

    firstRound = True
    p1grudgerCooperate, p2grudgerCooperate = True, True
    p2score, p1score, roundNo = 0, 0, 1
    p1coopHistory, p2coopHistory = [], []
    flag = isHuman()

    strategiesCom = [allCollude, allDefect, randomDecision, grudger, tft, suspiciousTft, reverseTft]
    strategiesRep = [allCollude, allDefect, randomDecision, grudgerRep, tftRep, suspiciousTftRep, reverseTftRep]

    playerMap = {
        "human" : humanPlayer,
        "computer" : random.choice(strategiesCom),
        "humanRep" : random.choice(strategiesRep)
    }

    while roundNo <= 10:  
        # match the agent function names according to the map
        p1Response = playerMap["human"]() if flag else playerMap["humanRep"]()
        p2Response = playerMap["computer"]()
        
        # update scores for both players based on the payoff matrix
        if p1Response and p2Response:
            p1score += 10
            p2score += 10
        elif p1Response and not p2Response:
            p1score += 0
            p2score += 20
        elif not p1Response and p2Response:
            p1score += 20
            p2score += 0
        elif not p1Response and not p2Response:
            p1score += 5
            p2score += 5
        
        p1coopHistory.append(p1Response)
        p2coopHistory.append(p2Response)
        
        print("\n---------------------------------")
        print(" Decision History & Score Board")
        print("---------------------------------")
        print("Human's decision: ", str(p1Response))
        print("Computer's decision: ", str(p2Response))
        
        print("\nHuman's cumalative score: ", str(p1score))
        print("Computer's cumulative score: ", str(p2score))
        print("\n\n")
        
        roundNo += 1
        firstRound = False
        
        # updates for grudger strategies
        if not p1Response and p2grudgerCooperate:
            p2grudgerCooperate = False
        if not p2Response and p1grudgerCooperate:
            p1grudgerCooperate = False

    # finalize
    marker(p1score, p2score) 
    if not flag:
        print("Human representative's strategy: ", str(playerMap["humanRep"].__name__)) 
    print("Computer's strategy: ", str(playerMap["computer"].__name__))  


if __name__ == "__main__":
	main()