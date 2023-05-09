from helper.constant import LoyaltyDB
from main import setUp

def devOperationGetQuery(file_name, sql_queries, sql_command):
    if LoyaltyDB(1).name.lower() in file_name:
        sql_queries[LoyaltyDB(1).name] = sql_command.read()
    if LoyaltyDB(2).name.lower() in file_name:
        sql_queries[LoyaltyDB(2).name] = sql_command.read()
    if LoyaltyDB(3).name.lower() in file_name:
        sql_queries[LoyaltyDB(3).name] = sql_command.read()
    if LoyaltyDB(4).name.lower() in file_name:
        sql_queries[LoyaltyDB(4).name] = sql_command.read()
    if LoyaltyDB(5).name.lower() in file_name:
        sql_queries[LoyaltyDB(5).name] = sql_command.read()
    if LoyaltyDB(6).name.lower() in file_name:
        sql_queries[LoyaltyDB(6).name] = sql_command.read()
    if LoyaltyDB(7).name.lower() in file_name:
        sql_queries[LoyaltyDB(7).name] = sql_command.read()
        
def prodOperationGetQuery(file_name, sql_queries, sql_command):
    if LoyaltyDB(8).name.lower() in file_name:
        sql_queries[LoyaltyDB(8).name] = sql_command.read()
    if LoyaltyDB(9).name.lower() in file_name:
        sql_queries[LoyaltyDB(9).name] = sql_command.read()
    if LoyaltyDB(10).name.lower() in file_name:
        sql_queries[LoyaltyDB(10).name] = sql_command.read()
    if LoyaltyDB(11).name.lower() in file_name:
        sql_queries[LoyaltyDB(11).name] = sql_command.read()
    if LoyaltyDB(12).name.lower() in file_name:
        sql_queries[LoyaltyDB(12).name] = sql_command.read()
    if LoyaltyDB(13).name.lower() in file_name:
        sql_queries[LoyaltyDB(13).name] = sql_command.read()
    if LoyaltyDB(14).name.lower() in file_name:
        sql_queries[LoyaltyDB(14).name] = sql_command.read()
        
def devOperationUpdateSP(db_name):
    if db_name == LoyaltyDB(1).name:
        connDb = setUp(LoyaltyDB(1).name)
    if db_name == LoyaltyDB(2).name:
        connDb = setUp(LoyaltyDB(2).name)
    if db_name == LoyaltyDB(3).name:
        connDb = setUp(LoyaltyDB(3).name)
    if db_name == LoyaltyDB(4).name:
        connDb = setUp(LoyaltyDB(4).name)
    if db_name == LoyaltyDB(5).name:
        connDb = setUp(LoyaltyDB(5).name)
    if db_name == LoyaltyDB(6).name:
        connDb = setUp(LoyaltyDB(6).name)
    if db_name == LoyaltyDB(7).name:
        connDb = setUp(LoyaltyDB(7).name)

    return connDb

def prodOperationUpdateSP(db_name):
    if db_name == LoyaltyDB(8).name:
        connDb = setUp(LoyaltyDB(8).name)
    if db_name == LoyaltyDB(9).name:
        connDb = setUp(LoyaltyDB(9).name)
    if db_name == LoyaltyDB(10).name:
        connDb = setUp(LoyaltyDB(10).name)
    if db_name == LoyaltyDB(11).name:
        connDb = setUp(LoyaltyDB(11).name)
    if db_name == LoyaltyDB(12).name:
        connDb = setUp(LoyaltyDB(12).name)
    if db_name == LoyaltyDB(13).name:
        connDb = setUp(LoyaltyDB(13).name)
    if db_name == LoyaltyDB(14).name:
        connDb = setUp(LoyaltyDB(14).name)

    return connDb