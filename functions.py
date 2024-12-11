import sqlite3
import pandas as pd
from config.config import config
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.preprocessing import LabelEncoder,OneHotEncoder




def reterive_clean_data(prompt):

    conn = sqlite3.connect(config.database_url)

    df_player = pd.read_sql_query(config.player_query,conn)
    df_team = pd.read_sql_query(config.team_query,conn)
    df_country = pd.read_sql_query(config.country_query,conn)
    df_match = pd.read_sql_query(config.match_query,conn)

    #print(df_player.columns[7])
    df_player.columns=['id_player', 'player_api_id', 'player_name', 'player_fifa_api_id', 'birthday', 'height', 'weight', 'id_attribute', 'player_fifa_api_id', 'player_id', 'date', 'overall_rating', 'potential', 'preferred_foot', 'attacking_work_rate', 'defensive_work_rate', 'crossing', 'finishing', 'heading_accuracy', 'short_passing', 'volleys', 'dribbling', 'curve', 'free_kick_accuracy', 'long_passing', 'ball_control', 'acceleration', 'sprint_speed', 'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina', 'strength', 'long_shots', 'aggression', 'interceptions', 'positioning', 'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle', 'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning', 'gk_reflexes']
    df_player.drop(config.drop_player, axis=1,inplace=True)   

    df_team.columns  = ['id_team', 'team_api_id', 'team_fifa_api_id', 'team_long_name', 'team_short_name', 'id_team_attribute', 'team_fifa_api_id', 'team_id', 'date', 'buildUpPlaySpeed', 'buildUpPlaySpeedClass', 'buildUpPlayDribbling', 'buildUpPlayDribblingClass', 'buildUpPlayPassing', 'buildUpPlayPassingClass', 'buildUpPlayPositioningClass', 'chanceCreationPassing', 'chanceCreationPassingClass', 'chanceCreationCrossing', 'chanceCreationCrossingClass', 'chanceCreationShooting', 'chanceCreationShootingClass', 'chanceCreationPositioningClass', 'defencePressure', 'defencePressureClass', 'defenceAggression', 'defenceAggressionClass', 'defenceTeamWidth', 'defenceTeamWidthClass', 'defenceDefenderLineClass']
    df_team.drop(config.drop_team, axis=1,inplace=True)
    df_team.drop(df_team.columns[1],axis=1,inplace=True)

    df_country.columns=['id','country_id','league_name','country_id','country_name']
    df_country.drop(config.drop_country,axis=1,inplace=True)

    df_match.drop(config.drop_match,axis=1,inplace=True)

    df_match = df_match.merge(df_country[['id', 'league_name', 'country_name']], left_on='country_id', right_on='id', how='left')
    df_match.drop('id_y',axis=1,inplace =True)
    df_match.columns=['id', 'country_id', 'season', 'stage', 'date', 'match_api_id', 'home_team_api_id', 'away_team_api_id', 'home_team_goal', 'away_team_goal', 'home_player_1', 'home_player_2', 'home_player_3', 'home_player_4', 'home_player_5', 'home_player_6', 'home_player_7', 'home_player_8', 'home_player_9', 'home_player_10', 'home_player_11', 'away_player_1', 'away_player_2', 'away_player_3', 'away_player_4', 'away_player_5', 'away_player_6', 'away_player_7', 'away_player_8', 'away_player_9', 'away_player_10', 'away_player_11', 'goal', 'shoton', 'shotoff', 'foulcommit', 'card', 'cross', 'corner', 'possession', 'league_name', 'country_name']
    new_df_team= df_team.drop_duplicates(subset='team_id')
    df_match = df_match.merge(new_df_team[['team_id', 'team_long_name']], left_on='home_team_api_id', right_on= 'team_id', how='left')
    df_match.rename(columns={'team_long_name': 'home_team'}, inplace=True)
    df_match.drop('team_id',axis=1,inplace=True)
    df_match = df_match.merge(new_df_team[['team_id', 'team_long_name']], left_on='away_team_api_id', right_on= 'team_id', how='left')
    df_match.rename(columns={'team_long_name': 'away_team'}, inplace=True)
    df_match.drop('team_id',axis=1,inplace=True)

    df_player['date'] = pd.to_datetime(df_player['date'])
    df_player['season'] = df_player['date'].apply(lambda x: f"{x.year}/{x.year + 1}" if x.month >= 8 else f"{x.year - 1}/{x.year}")

    df_player['potential'].fillna(df_player['potential'].mean(), inplace = True)
    df_player['overall_rating'].fillna(df_player['overall_rating'].mean(), inplace = True)
    # here you done evrething for analyse general

    if prompt == 'general':

        return df_match,df_team,df_player
    

    # here i start transforming data for model (outliers,standarization,encoding)
    # i need to  write the code here

    df_player['preferred_foot'] = df_player['preferred_foot'].fillna(df_player['preferred_foot'].mode()[0])
    df_player['attacking_work_rate'] = df_player['attacking_work_rate'].fillna(df_player['attacking_work_rate'].mode()[0])
    df_player['defensive_work_rate'] = df_player['defensive_work_rate'].fillna(df_player['defensive_work_rate'].mode()[0])


    df_player['positioning'] = df_player['positioning'].fillna(df_player['positioning'].median())
    df_player['penalties'] = df_player['penalties'].fillna(df_player['penalties'].median())
    df_player['finishing'] = df_player['finishing'].fillna(df_player['finishing'].median())
    df_player['crossing'] = df_player['crossing'].fillna(df_player['crossing'].median())
    df_player['short_passing'] = df_player['short_passing'].fillna(df_player['short_passing'].median())
    df_player['long_passing'] = df_player['long_passing'].fillna(df_player['long_passing'].median())
    df_player['shot_power'] = df_player['shot_power'].fillna(df_player['shot_power'].median())
    df_player['aggression'] = df_player['aggression'].fillna(df_player['aggression'].median())
    df_player['free_kick_accuracy'] = df_player['free_kick_accuracy'].fillna(df_player['free_kick_accuracy'].median())
    

    scaler = StandardScaler()
    df_player[['overall_rating',
    'potential',
    'height',
    'weight',
    'positioning',
    'penalties',
    'finishing',
    'crossing',
    'short_passing',
    'long_passing',
    'shot_power',
    'aggression',
    'free_kick_accuracy']]=scaler.fit_transform(df_player[['overall_rating',
    'potential',
    'height',
    'weight',
    'positioning',
    'penalties',
    'finishing',
    'crossing',
    'short_passing',
    'long_passing',
    'shot_power',
    'aggression',
    'free_kick_accuracy']])


    df_player['defensive_work_rate']=df_player['defensive_work_rate'].apply(lambda x : 'medium' if x not in ['medium','high','low'] else x)
    df_player['attacking_work_rate']=df_player['attacking_work_rate'].apply(lambda x : 'medium' if x not in ['medium','high','low'] else x)
    


    label_encoder =LabelEncoder()
    df_player['preferred_foot']=label_encoder.fit_transform(df_player['preferred_foot'])
    df_player['attacking_work_rate']=label_encoder.fit_transform(df_player['attacking_work_rate'])
    df_player['defensive_work_rate']=label_encoder.fit_transform(df_player['defensive_work_rate'])


    if prompt == 'player':
        return df_player
    


    team_int = ['buildUpPlaySpeed', 'buildUpPlayPassing', 'chanceCreationPassing', 'chanceCreationCrossing', 'chanceCreationShooting', 'defencePressure', 'defenceAggression']
    team_obj = ['buildUpPlaySpeedClass', 'buildUpPlayDribblingClass', 'buildUpPlayPassingClass', 'chanceCreationPassingClass', 'chanceCreationCrossingClass', 'chanceCreationShootingClass', 'defencePressureClass', 'defenceAggressionClass',  'defenceDefenderLineClass']
    
    df_team[team_int]=scaler.fit_transform(df_team[team_int])

    for ele in team_obj:
        df_team[ele]=label_encoder.fit_transform(df_team[ele])


    return df_team


    






    




