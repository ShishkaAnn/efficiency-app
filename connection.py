import pandas as pd
import sqlalchemy

# use this function to get a database engine
def GetEngine():
    url = 'mssql+pymssql://PCSRo01:GrKs0345@172.21.219.136:1433/PCS_RU'
    return sqlalchemy.create_engine(url)

# use this function to run a query
def run_query(qry):
    return pd.read_sql(sql=qry, con=GetEngine())






