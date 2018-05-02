

class MongoCommand:
    
    def __init__(self, mongohelper):
        self.__mongohelper = mongohelper

        
class CreateUser(MongoCommand):

    def __init__(self, mongohelper):
        super().__init(mongohelper)


    def __call__(self, name, email, password):
        users = self.__mongohelper.get_collection('users')
        new_user = { 'name': name, 'email': email, 'password': password }
        users.insert_onde(new_user)

        
