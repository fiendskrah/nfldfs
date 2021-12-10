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

def filter_byes(team_list, byes):
    playing_teams = [n for n in team_list if not any(m in n for m in byes)]
    return playing_teams

def create_contest(playing_teams, location_list):
    visiting_team = playing_teams[0::2]
    home_team = playing_teams[1::2]
    opponents = tuple(zip(visiting_team, home_team))
    contest = dict(zip(opponents, location_list))
    return contest