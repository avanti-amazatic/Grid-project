# we can store test data in this module like users

users = [
    {"name": "valid_user", "username": "avanti.d@amazatic.com", "password": "avanti.d"},
    {"name": "invalid_user", "username": "validUser@yahoo.com", "password": "ValidPassword"}
]


def get_user(name):
    try:
        return (user for user in users if user["name"] == name).next()
    except:
        print "\n     User %s is not defined, enter a valid user.\n" % name

