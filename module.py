def scoreboard(game):
    scoreboard = game.findAll('tr', attrs={'class':"shsMastScoreboardRow"})
    team_name0 = scoreboard[0].td.text
    quarter_scores0 = scoreboard[0].findAll('td', attrs={'class':"shsTotD"})
    final_score0 = quarter_scores0[4].text
    team_name1 = scoreboard[1].td.text
    quarter_scores1 = scoreboard[1].findAll('td', attrs={'class':"shsTotD"})
    final_score1 = quarter_scores1[4].text
    a=list((team_name0, final_score0, team_name1, final_score1))
    print(f"The final score is {a[0]} {a[1]}, {a[2]} {a[3]}.")

def playxplay(game):
    plays_list = []
    plays = game.findAll('div', attrs={'class':"shsPlayDetails"})
    for play in plays:
        plays = "(".join(play.text.split('('))
        plays_list.append(plays)
    print(f"There have been {len(plays_list)} plays in the game so far.")