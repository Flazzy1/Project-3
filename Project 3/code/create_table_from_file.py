import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import URL


urlib = URL.create(
    "postgresql",
    username="postgres",
    password="1234567",  
    host="localhost",
    database="test",
)

engine = create_engine(urlib)

df = pd.read_csv(r"A:\Data Engineering\Project 3\source\region.csv")

df.to_sql(name='region', con=engine, if_exists='replace')
