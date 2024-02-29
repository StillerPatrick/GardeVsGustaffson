import berserk
import constants

import matplotlib.pyplot as plt
import numpy as np
import statistics

session = berserk.TokenSession(constants.API_TOKEN)
client = berserk.Client(session=session)

first_game_date_epoch = 1686002400
non_video_games = 4
username_etienne = "ChessTienne"
username_jan = "JanistanTV"
game_list = client.games.export_by_player(username=username_etienne,
                                          vs=username_jan,
                                          since= first_game_date_epoch,
                                          moves=True,
                                          evals=True,
                                          sort="dateAsc")
games = list(game_list)
games = games[non_video_games:]

learning = []
for game in games:
    print(game)
    # print(first_game.keys())
    analysis = game["analysis"]
    players = game["players"]
    eddy_white = players["white"]["user"]["name"] == username_etienne
    print(players)
    game_score = []
    for i, a in enumerate(analysis):
        if "mate" in a.keys():
            continue
        score = a["eval"]
        if not eddy_white:
            score = score * -1
        game_score.append(score)
    learning.append(max(game_score))

    

learning = np.array(learning)
A = np.vstack([np.arange(1,len(games)+1), np.ones(len(games))]).T
m, c = np.linalg.lstsq(A, learning, rcond=None)[0]
print("m=",m)
plt.plot(np.arange(1,len(games)+1),learning, label="learning")
plt.plot(np.arange(1,len(games)+1),m*np.arange(1,len(games)+1) + c, label="linear regression")
plt.legend()
plt.grid()
plt.xlabel("Game")
plt.ylabel("Learning Score")
plt.show()