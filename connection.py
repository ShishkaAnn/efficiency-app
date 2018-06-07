import pandas as pd
import sqlalchemy

# use this function to get a database engine
def GetEngine():
    USER = 'YOUR_APIS_USER'
    PW = 'YOUR_APIS_PW'
    URL = '172.21.180.45:35432/ZEUS_RO'
    url = 'postgresql://{}:{}@{}'.format(USER,PW,URL)
    return sqlalchemy.create_engine(url)

# use this function to run a query
def run_query(qry):
    return pd.read_sql(sql=qry, con=GetEngine())







