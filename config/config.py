import yaml
from dotenv import load_dotenv
import os




load_dotenv()

class config():


    with open('config/config.yml','r') as file :
        config_data = yaml.load(file,Loader = yaml.FullLoader)


    account_user = config_data['DATA']['ACOUNT_DATABASE']
    player_query = config_data['QUERY']['PLAYER_QUERY']
    team_query = config_data['QUERY']['TEAM_QUERY']
    country_query = config_data['QUERY']['COUNTRY_QUERY']
    match_query = config_data['QUERY']['MATCH_QUERY']
    drop_player = config_data['COLUMNS']['DROP_PLAYER']
    drop_team = config_data['COLUMNS']['DROP_TEAM']
    drop_country = config_data['COLUMNS']['DROP_COUNTRY']
    drop_match = config_data['COLUMNS']['DROP_MATCH']
    keep_player = config_data['COLUMNS']['KEEP_PLAYER']
    keep_team = config_data['COLUMNS']['KEEP_TEAM']
    keep_match = config_data['COLUMNS']['KEEP_MATCH']
    cluster_player = config_data['COLUMNS']['CLUSTER_PLAYER']
    cluster_team = config_data['COLUMNS']['CLUSTER_TEAM']





    database_url = os.getenv('DATABASE_URL')






config = config()

#print(config.match_query)