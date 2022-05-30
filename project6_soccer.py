from random import randint,choice

# This class defines all methods for each player
class soccer_player:
  def __init__(self, name, task):
    self.name = name
    self.task = task
    self.goals = 0
    self.fouls = 0
  def __repr__(self):
    desc = "This is {name} a {task}. He has scored {goals} goals in his career and has made {fouls} fouls.\n".format(name=self.name, goals=self.goals, fouls=self.fouls, task=self.task)
    return desc

# This class defines all methods for each team
class soccer_team:
  def __init__(self, name, players):
    self.name = name
    self.goal_keeper = players[0]
    self.defender = players[1]
    self.striker = players[2]
    self.goal_percentages = choice([0.7, 0.75, 0.8, 0.85, 0.9])
    self.leagues_won = []
  def __repr__(self):
    desc = "This team is {name}. The goal keeper is {keeper}, defender is {defender} and striker is {striker}.\n".format(name=self.name, keeper=self.goal_keeper.name, defender=self.defender.name, striker=self.striker.name)
    desc += f"They have won {len(self.leagues_won)} leagues, including: "
    for leag in self.leagues_won:
        desc += f"{leag}, "
    desc = desc[:-2]
    return desc

# This class defines all methods for each league
class league:
  league_players={}
  def __init__(self, name, teams):
    self.name = name
    self.teams = teams
    self.rankings ={key:[0,0,0,0,0,0,0,0] for key in teams}
    self.initial_teams = [team for team in self.teams]
    self.find_number_of_games()
    for team in teams:
      self.league_players[team.striker] = [team.name, 0]
      self.league_players[team.defender] = [team.name, 0]

  # This calculates the number of games in a league
  def find_number_of_games(self):
    n = len(self.teams)
    games = n-1
    for i in range(n-2, 0, -1):
      games += i
    self.games = games
  i = 0

  # Runs all the games in the league
  def make_game(self, teams_list,see_results="n"):
    if teams_list == []:
      teams_list = self.initial_teams
    home = teams_list[0]
    for index in range(1, len(teams_list)):
      away = teams_list[index]
      
      home_game = game(home, away); home_game.play_game()
      self.update_rankings(home_game.scores)
      
      print(f"{home.name}  {home_game.scores[home]}:{home_game.scores[away]}  {away.name}")
      if see_results == "y":
        self.print_league_results()
      # print(home_game.scores)
      user = input()
      away_game = game(away, home); away_game.play_game()
      self.update_rankings(away_game.scores)
      # print(away_game.scores)
      print(f"{away.name}  {away_game.scores[away]}:{away_game.scores[home]}  {home.name}")
      if see_results == "y":
        self.print_league_results()
      
      user = input()
    if len(teams_list)>2:
      self.make_game(teams_list[1:], "y")
  
  # Updates league rankings after each game
  def update_rankings(self, scores):
    home = list(scores)[0]
    away = list(scores)[1]
    # rankings {team:[games played, wins, draw, lose goals scored, goals away, points]}
    
    for team in [home, away]:
      self.rankings[team][0] += 1
      self.rankings[team][-4] += scores[team]
    self.rankings[home][-3] += scores[away]
    self.rankings[away][-3] += scores[home]
    self.rankings[home][-2] = self.rankings[home][-4]-self.rankings[home][-3]
    self.rankings[away][-2] = self.rankings[away][-4]-self.rankings[away][-3]
    if scores[home] > scores[away]:
      self.rankings[home][1] +=1
      self.rankings[home][-1]+=3
      self.rankings[away][3] +=1
    elif scores[home] < scores[away]:
      self.rankings[away][1] +=1
      self.rankings[away][-1] +=3
      self.rankings[home][3] +=1
    else:
      self.rankings[away][2] += 1
      self.rankings[home][2] += 1
      self.rankings[home][-1] +=1
      self.rankings[away][-1] +=1
    # print(self.rankings)
  
  # Update player statistics after league ends
  def update_player_stats(self):
    for team in self.rankings:
      goals = self.rankings.get(team)[-4]
      percentage = team.goal_percentages
      striker_goals = int(goals*percentage);
      defender_goals = goals - striker_goals
      team.striker.goals += striker_goals
      self.league_players[team.striker][-1] += striker_goals
      team.defender.goals += defender_goals
      self.league_players[team.defender][-1] += defender_goals
      print(team.striker.name, team.striker.goals)
  
  # Displays league rankings table
  def print_league_results(self):
    # rankings {team:[games played, wins, draw, lose goals scored, goals away, points]}
    row = ["Teams","G","W","D","L","GF","GA","GD","P"]
    i = 0
    all_rows = []
    for team in self.rankings:
      if i == 0:
        i+=1
        row_to_print = row[0].ljust(15, "_")
        for element in row[1:]:
          row_to_print += element.center(4,"_")  
        print(row_to_print) 

      row = [team.name]+self.rankings.get(team)
      row = row[-1:]+[row[-2]]+row[:-2]
      all_rows.append(row)
    all_rows.sort(reverse=True)
    self.winner = {all_rows[0][2]:all_rows[0][0]}
    for row in all_rows:
      row_to_print = row[2].ljust(15)
      for element in row[3:]:
        row_to_print += str(element).center(4)
      row_to_print += str(row[1]).center(4)+str(row[0]).center(4)
      print(row_to_print)
    print("") 
      # print(row[0].ljust(13))
    # print(c0.ljust(13)+c1.center(4)+c2.center(4)+c3.center(4)+c4.center(4)+c5.center(4)+c6.center(4)+c7.center(4))

  # Displays goal rankings table
  def print_goal_rankings(self):
    all_rows = []
    for player in self.league_players:
      all_rows.append([self.league_players[player][1], player.name, self.league_players[player][0]])
    
    all_rows.sort(reverse=True)
    self.best_goal_scorer = {all_rows[0][1]:[all_rows[0][0], all_rows[0][2]]}
    row1 = ["Player","Team", "Goals"]; i = 0
    for row in all_rows:
      if i == 0:
        print(row1[0].ljust(15,'_')+row1[1].ljust(15,'_')+row1[2].center(6,'_'))
        i += 1
      print(row[1].ljust(15)+row[2].ljust(15)+str(row[0]).center(6))
    

  def __repr__(self):
    desc = "This league is called {name}. It has {number_of_teams} teams and {number_of_games} games.".format(name=self.name, number_of_teams=len(self.teams), number_of_games=self.games)
    return desc

# This defines all the methods for each game
class game:
  def __init__(self, home, away):
    self.home = home
    self.away = away
    self.scores = {}
    self.scores[home] = 0
    self.scores[away] = 0
  
  steps_to_score = 3
  available_number_of_steps = 100
  remaining_number_of_steps = 300

  # Simulates each game
  def play_game(self):
    self.home_possession(2)
    self.scores[self.home] = int(self.scores[self.home]/20)
    self.scores[self.away] = int(self.scores[self.away]/20)
    return
  
  # Simulates the home team during a game
  def home_possession(self, away_remainder):
    home_present_step = self.steps_to_score - away_remainder
    while home_present_step >= 0:
      possession_winner = self.fight_for_possession()
      if possession_winner == 1:
        self.away_possession(home_present_step)
        return
      home_present_step -= 1
      if self.are_steps_available() == False:
        return
    self.scores[self.home]+=1
    self.home_possession(2)
    return

  # simulates the away team during a game
  def away_possession(self, home_remainder):
    away_present_step = self.steps_to_score - home_remainder
    while away_present_step >= 0:
      possession_winner = self.fight_for_possession()
      if possession_winner == 0:
        self.home_possession(away_present_step)
        return
      away_present_step -= 1
      if self.are_steps_available() == False:
        return
    self.scores[self.away]+=1
    self.away_possession(2)

  # Defines which team wins possession during each attack
  def fight_for_possession(self):
    possession_winner = choice([0, 1])
    return possession_winner

  # Determines the end of each game
  def are_steps_available(self):
    self.remaining_number_of_steps -= 1
    if self.remaining_number_of_steps == 0:
      return False
    return True

#_______________________________________________________
#_______________________________________________________


### All players in the game
strikers = [soccer_player("Neymar", "striker"),soccer_player("Messi", "striker"),soccer_player("Mbappe", "striker"),soccer_player("Ronaldo", "striker"),soccer_player("Lewandoski", "striker"),soccer_player("Firmino", "striker")]

defenders = [soccer_player("Van_djik", "defender"),soccer_player("Leonardo", "defender"),soccer_player("Pique", "defender"),  soccer_player("Luiz", "defender"),soccer_player("Julian", "defender"),soccer_player("Ramos", "defender")]

goalkeepers = [soccer_player("Handanovic", "goalkepper"),soccer_player("Martinez", "goalkeeper"),soccer_player("Moraes", "goalkeeper"),soccer_player("Neuer", "goalkeeper"),soccer_player("Becker", "goalkeeper"),soccer_player("Donnarumma", "goalkeeper")]

all_players = strikers+defenders+goalkeepers

### All teams in the game
team_names = ["Real Madrid", "Valencia", "PSG", "Barcelona", "Bayern Munchen", "Juventus"]
all_teams = []
number_of_teams = len(strikers)-1;
# randomly assign players to each team
while number_of_teams >= 0:
  team_ind = randint(0,number_of_teams)
  player_ind = randint(0, number_of_teams)
  all_teams.append(soccer_team(team_names.pop(team_ind), [goalkeepers.pop(player_ind),defenders.pop(player_ind),strikers.pop(player_ind)]))
  number_of_teams -= 1

#_______________________________________________________
#_______________________________________________________

# Creates a custom league
def create_league(name, desired_number_of_teams):
  league_teams_pool = [team for team in all_teams]
  selected = 0; available_teams = len(league_teams_pool)
  selected_teams = []; pop_index = len(league_teams_pool)-1
  while available_teams > 0:    
    selected_teams.append(league_teams_pool.pop(randint(0,pop_index)))
    selected += 1
    if selected == desired_number_of_teams:
      break
    pop_index -=1

  
  new_league = league(name, selected_teams)
  return new_league

# Display league results
def closure_stats(league):
  winning_team = list(league.winner)[0]
  best_scorer = list(league.best_goal_scorer)[0]
  for team in all_teams:
    if team.name == winning_team:
      team.leagues_won.append(league.name)
  print(f"\nLeague winner: {winning_team}, {league.winner[winning_team]} points")
  print(f"Highest goal scorer: {best_scorer} ({league.best_goal_scorer[best_scorer][-1]})  {league.best_goal_scorer[best_scorer][0]}")

# This block of code runs until user exits program
while True:
  user_input = input("Do you want to watch a league? (y or n) ")
  if user_input.lower().strip() == "y":
    league_name = input("Enter the name of the league: ").strip().title()
    desired_teams = int(input("Enter the number of teams (atmost 6): "))
    new_league =  create_league(league_name, desired_teams)
    see_game_results = input("Would you like to see league results after each game results? (y or n) ")
    new_league.make_game([], see_game_results)
    new_league.update_player_stats()
    new_league.print_league_results()
    new_league.print_goal_rankings()
    closure_stats(new_league)

    see_player_stats = input("Do you want to see player stats? (y or n) ")
    if see_player_stats == "y":
      while True:
        name = input("Enter player name: ")
        if name == "stop":
          break
        for player in all_players:
          if player.name == name:
            print(player)

    see_team_stats = input("Do you want to see team stats? (y or n) ")
    if see_team_stats == "y":
      while True:
        name = input("Enter team name: ")
        if name == "stop":
          break
        for team in all_teams:
          if team.name == name:
            print(team)
  else:
    break
