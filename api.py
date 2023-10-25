from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import pandas as pd
from datetime import datetime

from db_config import DB_CONFIG

class DatabaseAPI:
    def __init__(self):
        self.engine = create_engine(
            f'postgresql://{DB_CONFIG["user"]}:{DB_CONFIG["password"]}@{DB_CONFIG["host"]}/{DB_CONFIG["database"]}'
        )
        self.Session = sessionmaker(bind=self.engine)


    @staticmethod
    def measure_time(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            result = func(*args, **kwargs)
            end_time = datetime.now()
            print(f"Execution time: {end_time - start_time}")
            return result

        return wrapper

    @measure_time
    def create_table(self, dataframe, table_name):
        dataframe.to_sql(table_name, self.engine, if_exists="replace", index=False)

    @measure_time
    def delete_from_table(self, table_name, conditions):
        query = text(f"DELETE FROM {table_name} WHERE {conditions}")
        session = self.Session()
        session.execute(query)
        session.commit()
        session.close()

    @measure_time
    def truncate_table(self, table_name):
        session = self.Session()
        session.execute(text(f"TRUNCATE TABLE {table_name}"))
        session.commit()
        session.close()

    @measure_time
    def read_sql(self, query):
        return pd.read_sql(query, self.engine)

    @measure_time
    def insert_sql(self, dataframe, table_name, mode):
        dataframe.to_sql(table_name, self.engine, if_exists=mode, index=False)

    def execute(self, query):
        session = self.Session()
        result = session.execute(text(query))
        session.commit()
        session.close()
        return result
