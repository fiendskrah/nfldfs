# using NBCsports.com to scrape nfl box scores/stats for fantasy points

game url (completed): https://scores.nbcsports.com/fb/boxscore.asp?gamecode=20211121016&home=16&vis=9&final=true#

game url (in progress):  https://scores.nbcsports.com/fb/boxscore.asp?gamecode=20211121024&home=24&vis=23&meta=true# 

base = 'scores.nbcsports.com/fb/boxscore.asp?'
game = 'gamecode=[date of game]'
home team = '&home=[teamcode]'
   * [ ] team = '&vis=[teamcode]'
if game is over = '&final=true#'
if game is not over ='&meta=true' 



stats per player on game page
element on game page for player contains link to players page - can leverage to pull full name 
