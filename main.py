import os
import conf.config as config
import helper.path as file_path
import helper.operation as db
from dotenv import load_dotenv
from helper.connection import Connection
from sqlalchemy import text

# load .env file 
load_dotenv()
stage = os.getenv("STAGE")

# static dict / hash variable definition for put all queries
sql_queries = {}


def setUp(db_name):
    if stage == "development":
        set_db = config.setDbConfig(db_name, stage)
    if stage == "production":
        set_db = config.setDbConfig(db_name, stage)

    connection = Connection(set_db)
    
    # validate connection to DB
    if connection.test_engine() == None:
        print("Connected Succesfully Captain :)")
    else:
        print("Opss There is Some Trouble Captain :( ")
    
    return connection
            
def getQuery():
    # try to get all SQL Command from text files
    for filename in os.listdir(file_path.RELATIVE_PATH):
        # get all lists of file
        f = os.path.join(file_path.RELATIVE_PATH, filename)
        if os.path.isfile(f):
            # loop through each file
            with open(f) as sql_command:
                if stage == "development":
                    db.devOperationGetQuery(f, sql_queries, sql_command)
                if stage == "production":
                    db.prodOperationGetQuery(f, sql_queries, sql_command)

def main():    
    # get all list of query
    getQuery()
    
    # # update query in all db
    for db_name, query in sql_queries.items():
        if stage == "development":
            connDb = db.devOperationUpdateSP(db_name)
        if stage == "production":
            connDb = db.devOperationUpdateSP(db_name)
            
        # try to create Store Procedure to DB 
        with connDb.get_engine().connect() as connection:
            # loop through each query and execute the query
            connection.execute(text(
                query
            ))
            connection.commit()
            
        print(f"Yeayy, Successfully Update the SP in {db_name} Database Captain \n")

if __name__ == '__main__':
    main()