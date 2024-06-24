import pandas as pd
from sklearn.model_selection import train_test_split
import os

def prepare_data(data, player_name, limit_points):
    player_data = data[data['Player'] == player_name].copy()
    player_data.loc[:, 'Above_Limit'] = player_data['PTS'] > limit_points
    train_data = player_data.iloc[:-1]
    test_data = player_data.iloc[-1:]


    features = ['MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 
            'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 
            'STL', 'BLK', 'TOV', 'PF']
    
    X_train = train_data[features]
    y_train = train_data['Above_Limit']

    X_test = test_data[features]
    y_test = test_data['Above_Limit']
    y_test_pts = test_data['PTS'].values[0]

    return X_train, y_train, X_test, y_test, y_test_pts

def list_players(data):

    players = data['Player'].unique()
    
    with open('players_list.txt', 'w') as file:
        for player in players:
            file.write(f"{player}\n")

    os.system('less players_list.txt')



def load_data(filepath):
    data = pd.read_csv(filepath)
    data = data.sort_values(by='Data', ascending=True)
    selected_columns = ['Player', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 
                    'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 
                    'BLK', 'TOV', 'PF', 'PTS']
    
    new_data = data[selected_columns]
    games_per_player = new_data['Player'].value_counts()
    eligible_players = games_per_player[games_per_player >= 16].index
    filtered_data = new_data[new_data['Player'].isin(eligible_players)]

    return filtered_data