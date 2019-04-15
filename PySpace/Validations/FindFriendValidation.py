from DataAccessLayer import ViewFriendsDB
'''validate whether two people are friend of each other or not'''

def validate_is_two_friends(username,friendname):
    if ViewFriendsDB.check_friends(username, friendname)>0:
        return True
    return False