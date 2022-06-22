

def main():
    competitions = [
        ["Bulls", "Eagles"],
        ["Bulls", "Bears"],
        ["Bears", "Eagles"]
        ]
    results = [0, 0, 0]
    print(tournamentWinner2(competitions, results))
    
  
def tournamentWinner(competitions, results):
    teamsPoints = {}
    for i in range(len(competitions)):
        if results[i] == 1:
            matchWinner = competitions[i][0]
            if matchWinner in teamsPoints:
                teamsPoints[matchWinner] += 3
            else:
                teamsPoints[matchWinner] = 3
        else:
            matchWinner = competitions[i][1]
            if matchWinner in teamsPoints:
                teamsPoints[matchWinner] += 3
            else:
                teamsPoints[matchWinner] = 3
        
    #max_points = max(teamsPoints.values())
    #comp_winner = [k for k, v in teamsPoints.items() if v == max_points]
    comp_winner = max(teamsPoints, key=teamsPoints.get)
    return  comp_winner

def tournamentWinner2(competitions, results):
    bestTeam = ""
    scores = {bestTeam : 0}
    for i in range(len(competitions)):
        if results[i] == 1:
            matchWinner = competitions[i][0]
            if matchWinner in scores:
                scores[matchWinner] += 3
            else:
                scores[matchWinner] = 3
        else:
            matchWinner = competitions[i][1]
            if matchWinner in scores:
                scores[matchWinner] += 3
            else:
                scores[matchWinner] = 3

        if scores[bestTeam] < scores[matchWinner]:
            bestTeam = matchWinner
        
    return  bestTeam
  
  
  
  
    
if __name__ == "__main__":
    main()