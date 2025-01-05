from nba_api.stats.static import teams
import matplotlib.pyplot as plt
import pandas as pd


def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

nba_teams = teams.get_teams()

print("the teams(0:3) are: ", nba_teams[0:3])

dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)
print("df teams head is: ", df_teams.head())

df_warriors=df_teams[df_teams['nickname']=='Warriors']
print("df warriors is: ", df_warriors)


id_warriors=df_warriors[['id']].values[0][0]
# we now have an integer that can be used to request the Warriors information 
print("id warriors is: ", id_warriors)

from nba_api.stats.endpoints import leaguegamefinder

# Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is commented out, you can run it on jupyter labs on your own computer.
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)


# Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is commented out, you can run it on jupyter labs on your own computer.
# gamefinder.get_json()

# Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is comment out, you can run it on jupyter labs on your own computer.
games = gamefinder.get_data_frames()[0]
print("games_head is: ", games.head())

import requests

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

download(filename, "Golden_State.pkl")


file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
print("games head is again: ", games.head())


games_home=games[games['MATCHUP']=='GSW vs. TOR']
games_away=games[games['MATCHUP']=='GSW @ TOR']

print(games_home['PLUS_MINUS'].mean())


print(games_away['PLUS_MINUS'].mean())

fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()

