

def main():
    competitions = [
        ["Bulls", "Eagles"],
        ["Bulls", "Bears"],
        ["Bears", "Eagles"]
        ]
    results = [0, 0, 0]
    print(tournamentWinnerOptimal(competitions, results))
    
  
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


HOME_TEAM_WON = 1

def tournamentWinnerOptimal(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}
    
    for idx, match in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = match
        
        matchWinner = homeTeam if result == HOME_TEAM_WON else awayTeam
        
        updateScore(matchWinner, 3, scores)
        
        if scores[matchWinner] > scores[currentBestTeam]:
            currentBestTeam = matchWinner

    return currentBestTeam

def updateScore(team, points, scores):
    if team not in scores:
        scores[team] = 0
    
    scores[team] += points
  
  
  
    
if __name__ == "__main__":
    main()