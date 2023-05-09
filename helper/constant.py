from enum import Enum

class LoyaltyDB(Enum):
    # list dev db name of loyalty
    Loyalty_Chilgo_Dev = 1
    Loyalty_KBN_Dev = 2
    Loyalty_KECC_Dev = 3
    Loyalty_KLB_Dev = 4
    Loyalty_Kalcare_Dev = 5
    Loyalty_MiniTools_Dev = 6
    Loyalty_SHP_Dev = 7
        
    # list prod db name of loyalty
    Loyalty_Chilgo_Prod = 8
    Loyalty_KBN_Prod = 9
    Loyalty_KECC_Prod = 10
    Loyalty_KLB_Prod = 11
    Loyalty_Kalcare_Prod = 12
    Loyalty_MiniTools_Prod = 13
    Loyalty_SHP_Prod = 14

def getDevDb(number):
    return LoyaltyDB(number).name

def getProdDb(number):
    return LoyaltyDB(number).name