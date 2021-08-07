import pandas as pd
from sqlalchemy import create_engine

def get_csv(data):
    """
    This function takes a csv file and converts it to a dataframe
    """

    df = pd.read_csv(data)
    return df


def connect_to_db(user, password, host, database):
    """
    This function connects to your heroku postgres database
    """

    engine = create_engine(f'postgresql://{user}:{password}@{host}/{database}')
    return engine

    

