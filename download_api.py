from config.config import config
import kaggle 


# first you need to create a .kaggle folder then move kaggle.jsoon to this folder 


kaggle.api.authenticate()

kaggle.api.dataset_download_files(config.account_user,path='./data',unzip=True)

